$(document).ready(function() {
	$(chart_id).highcharts({
		
		title: title,
		xAxis: xAxis,
		yAxis: yAxis,
		series: series,
		subtitle: subtitle,
		tooltip: tooltip,
		legend: legend
		
	});
});