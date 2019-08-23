$(document).ready(function() {
	$(chart_id).highcharts({
        chart: chart,       
        title: title,
        subtitle: subtitle,
        tooltip: tooltip,
        xAxis: xAxis, 
		yAxis: yAxis,
		series: series,
        plotOptions: plotOptions,
        legend: legend,
        credits: credits        
	});
});