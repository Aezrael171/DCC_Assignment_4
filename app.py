from flask import Flask, redirect, url_for, request, Response, render_template, jsonify, json
from flask_mysqldb import MySQL



app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'PLexi90556T!'
app.config['MYSQL_DB'] = 'redemption'

mysql = MySQL(app)

@app.route('/', methods=["POST", "GET"])
def main_page():
    return render_template("index.html")

@app.route('/find', methods=["POST", "GET"])
def search_main_page():
    return render_template("finder.html")

@app.route('/find/result', methods=["POST"])
def search():
    if request.method == "POST":
        selected_column = request.form['search_column']
        selected_table = request.form['search_table']
        search_term = request.form['search_term']
      
        if selected_column and search_term:
            cursor = mysql.connection.cursor()

            if selected_table == 'purchase':
                
                cursor.execute(f"SELECT * FROM purchase WHERE {selected_column} = %s", (search_term,))
            elif selected_table == 'redemption':
                cursor.execute(f"SELECT * FROM redemption WHERE {selected_column} = %s", (search_term,))
            search_results = cursor.fetchall()
            cursor.close()
            column_headers = [
                'Reference No',
                'Journal Date',
                'Date of Purchase',
                'Date of Expiry',
                'Purchaser',
                'prefix',
                'Bond Number',
                'denominations',
                'issue Branch Code',
                'Issue Teller',
                'Status'  
            ] if selected_table == 'purchase' else [
                'Date of Encashment',
                'Political Party',
                'Account No',
                'prefix',
                'Bond Number',
                'Denominations',
                'Pay Branch Code',
                'Pay Teller'
            ]
           
            return render_template("finder.html", search_results=search_results, selected_column=selected_column, column_headers=column_headers, selected_table=selected_table)
@app.route('/tracker')
def analyze_main():
    return render_template('tracker.html')

@app.route('/tracker/result', methods=['POST'])
def tracker():
    if request.method == "POST":
        political_party = request.form['political_party']
        if political_party:
            cursor = mysql.connection.cursor()
            format = '%d/%M/%Y'
            cursor.execute(f"SELECT YEAR(STR_TO_DATE(Date_of_Encashment,'%d/%M/%Y')) AS year, COUNT(*) AS num_bonds,SUM(denominations) AS total_value FROM redemption WHERE Name_of_party = '{political_party}' GROUP BY YEAR(STR_TO_DATE(Date_of_Encashment,'%d/%M/%Y'))")
            data = cursor.fetchall()
            cursor.close()
         
            years, num_bonds, total_value = [], [], []
            for row in data:
                years.append(row[0])
                num_bonds.append(row[1])
                total_value.append(row[2])
            return render_template('tracker.html', years=years, num_bonds=num_bonds, total_value=total_value)
        else:
            return render_template('tracker.html')

@app.route('/company')
def company_main():
    return render_template('company.html')

@app.route('/company/result', methods=['POST'])
def analyze_company():
    if request.method == "POST":
        company = request.form['company']
        if company:
            cursor = mysql.connection.cursor()
            format = '%d/$M/%Y'
            cursor.execute(f"SELECT YEAR(STR_TO_DATE(date_of_purchase,'%d/%M/%Y')) AS year, COUNT(*) AS num_bonds,SUM(denominations) AS total_value FROM purchase WHERE  name_of_purchaser= '{company}' GROUP BY YEAR(STR_TO_DATE(date_of_purchase,'%d/%M/%Y'))")
            
            data = cursor.fetchall()
            cursor.close()

            years, num_bonds, total_value = [], [], []
            for row in data:
                years.append(row[0])
                num_bonds.append(row[1])
                total_value.append(row[2])

            return render_template('company.html', years=years, num_bonds=num_bonds, total_value=total_value)
    else:
        return render_template('company.html')

@app.route('/pichart')
def pichart():

    cursor = mysql.connection.cursor()
    cursor.execute("SELECT Name_of_party, sum(denominations) FROM redemption GROUP BY Name_of_party")
    data = cursor.fetchall()
    cursor.close()

    political_parties = []
    denominations = []
   
    for row in data:
        political_parties.append(row[0])
        denominations.append(row[1])

    return render_template('pichart.html', political_parties=political_parties, denominations=denominations)

@app.route('/partydataplot')
def alluvialparty():
    return render_template("partydataplot.html")
@app.route('/partydataplot/result', methods=['POST','GET'])
def alluvialpartychart():
    alluvialpartydata = request.form['alluvialparty']
    if request.method == "POST":
        if alluvialpartydata:
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT purchase.name_of_purchaser, SUM(redemption.denominations) as total, redemption.Name_of_party FROM redemption JOIN purchase ON redemption.prefix = purchase.prefix AND redemption.bond_number = purchase.bond_no where Name_of_party = %s GROUP BY purchase.name_of_purchaser", (alluvialpartydata,))
            query_data = cursor.fetchall()
            cursor.close()

            data = []
            
            for row in query_data:
                data.append({"from": row[0  ], "to": row[2], "value": row[1]})
           

            return render_template('partydataplot.html', chart_data=json.dumps(data),query_data=query_data)


    else:
        return render_template('partydataplot.html', data=None)

@app.route('/companydataplot')
def alluvialcompany():
    return render_template("companydataplot.html")
@app.route('/companydataplot/result', methods=['POST','GET'])
def alluvialcompanychart():
    alluvialcompanydata = request.form['alluvialcompany']
    if request.method == "POST":
        if alluvialcompanydata:
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT Name_of_party, SUM(purchase.denominations) as total, name_of_purchaser FROM purchase JOIN redemption ON redemption.prefix = purchase.prefix AND redemption.bond_number = purchase.bond_no where name_of_purchaser = %s GROUP BY Name_of_party", (alluvialcompanydata,))
            query_data = cursor.fetchall()
            cursor.close()

     
            data = []
           
            for row in query_data:

                data.append({"from": row[2], "to": row[0], "value": row[1]})
        

            return render_template('companydataplot.html', chart_data=json.dumps(data),query_data=query_data)


    else:
        return render_template('companydataplot.html', data=None)
if __name__ == '__main__':
    app.run(host="0.0.0.0", port="80", debug=True)
