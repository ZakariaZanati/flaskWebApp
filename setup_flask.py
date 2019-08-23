from flask import Flask , render_template , url_for
from py2neo import Graph , Node , Relationship
import json

app = Flask(__name__)
graph = Graph()


@app.route("/")
@app.route("/Acceuil")
def Acceuil():
    return render_template('home.html')

@app.route("/about")
def about():


    


    return render_template('about.html')

@app.route("/indicateurs1")
def indicateurs1(chartID = 'chart_ID'):

    query = """
    match(p:Publication)-[:PUBLISHED_BY]->(n:Author)-[:AFFILIATED]->(m:Affiliation)  
    where p.date > 2015 and p.date < 2019
    return m.name as name ,m.country ,count(m)
    order by count(m) desc
    limit 20
    """

    data = graph.cypher.execute(query)

    publications = []

    
    for row in data:
        publications+=[[row[0],row[2]]]

    chart = { "type": 'column'}
    xAxis = { "type": "category", "labels": { "rotation": -45, "style": { "fontSize" : '13px',"fontFamily": 'Verdana, sans-serif'}}}
    yAxis = {"min": 0,"title": {"text": 'number of publications'}}
    title = {"text" : 'publications by affiliations from 2015 to 2018'   }
    tooltip = {"pointFormat": 'Publications: <b>{point.y:.1f} millions</b>'}
    series = [{"name": 'Publications',"data": publications,"dataLabels": {"enabled": "true","rotation": -90,"color": '#FFFFFF',"align": 'right',"format": '{point.y:.1f}', "y": 10, "style": {"fontSize": '13px',"fontFamily": 'Verdana, sans-serif'}}}]
    subtitle = {"text": 'Source: <a href = "https://www.scopus.com/home.uri">Scopus</a>'}
    credit = {"enabled": "true"} 

    return render_template('indicateurs1.html', chartID=chartID,chart=chart, credits=credit ,series=series, title=title, xAxis=xAxis, yAxis=yAxis , tooltip=tooltip, subtitle=subtitle)

@app.route("/indicateurs2")
def indicateurs2(chartID = 'chart_ID'):


    names = ["University of Oklahoma", "University of Chicago", "Washington University School of Medicine in St. Louis","Stanford University","University of California, San Diego"]

    nb_publications=[]

    for  name in names:
    
        query = """
        match(p:Publication)-[:PUBLISHED_BY]->(n:Author)-[:AFFILIATED]->(m:Affiliation { name: "%s" } )  
        where p.date > 2014 and p.date < 2019 
        return  p.date, count(p)  
        order by p.date
        """%(name)

        data=graph.cypher.execute(query)

        nb=[]

        for row in data:
            nb+=[row[1]]
        
        nb_publications+=[nb]

    title = { "text": 'Nombre de publications par année ' }  
    subtitle = {"text": 'Source: Scopus.com' }
    xAxis = { "categories": ['2015', '2016', '2017', '2018'] }
    yAxis = {"title": {"text": 'Nombres de publications' },"plotLines": [{"value": 0,"width": 1,"color": '#808080'}]}
    tooltip = {"valueSuffix": '\xB0'} 
    legend = { "layout": 'vertical', "align": 'right', "verticalAlign": 'middle', "borderWidth": 0}
    series =  [{"name": names[0],"data": nb_publications[0]}, {"name": names[1],"data": nb_publications[1]},{"name": names[2],"data": nb_publications[2]},{"name": names[3],"data": nb_publications[3]},{"name": names[4],"data": nb_publications[4]}]
    return render_template('indicateurs2.html', chartID=chartID,series=series, title=title, xAxis=xAxis, yAxis=yAxis , tooltip=tooltip, subtitle=subtitle, legend=legend)



@app.route("/indicateurs3")
def indicateurs3(chartID = 'chart_ID'):
    query = """
        match(p:Publication)-[:PUBLISHED_BY]->(n:Author)-[:AFFILIATED]->(m:Affiliation  )  
        where p.date > 2014 and p.date < 2019
        return  m.country, count(p)  
        order by count(p) desc 
        limit 5
    """
    data=graph.cypher.execute(query)

    names = [row[0] for row in data]

    year_2015 = []
    year_2016 = []
    year_2017 = []
    

    for  name in names:
        
        query = """
        match(p:Publication)-[:PUBLISHED_BY]->(n:Author)-[:AFFILIATED]->(m:Affiliation {country: "%s"} )  
        where p.date > 2014 and p.date < 2018
        return   count(p), p.date
        order by p.date
        """%(name)

        data = graph.cypher.execute(query)

        year_2015+= [data[0][0]]
        year_2016+= [data[1][0]]
        year_2017+= [data[2][0]]
      
    
    chart = {"type": 'bar'}                        
    title = {"text": 'Top 5 pays : publications par année '}
    subtitle = {"text": 'Source: scopus.com'  }
    xAxis = {"categories": names,"title": {"text": "pays"}}
    yAxis = {"min": 0,"title": {"text": 'Nombre de publications',"align": 'high'},"labels": {"overflow": 'justify'}}
    tooltip = {"valueSuffix": ' publications'}
    plotOptions = {"bar": {"dataLabels": {"enabled": "true"}}}
    legend = {"layout": 'vertical',"align": 'right',"verticalAlign": 'top',"x": -40,"y": 100,"floating": "true","borderWidth": 1,"backgroundColor":  '#FFFFFF'}
    credit = {"enabled": "false"}
    series = [{"name": 'Year 2015',"data":year_2015 }, {"name": 'Year 2016',"data":year_2016 }, {"name": 'Year 2017',"data":year_2017  }]

    return render_template('indicateurs3.html', chartID=chartID,chart=chart, credits=credit ,series=series, title=title, xAxis=xAxis, yAxis=yAxis , tooltip=tooltip, subtitle=subtitle,legend=legend,plotOptions=plotOptions)

if __name__ == "__main__":
    app.run(debug=True)


	




