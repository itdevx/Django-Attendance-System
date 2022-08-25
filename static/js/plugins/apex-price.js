(function ($) {

    let ajaxUrl = "https://min-api.cryptocompare.com/data/histoday?fsym=BTC&tsym=USD&limit=30";
    let dataSet = [];

    function ajax_request(url) {
	let xhttp;
	xhttp = new XMLHttpRequest();

	xhttp.onreadystatechange = function () {
	    if (this.readyState == 4 && this.status == 200) {
		handle_chart(this.responseText);
	    }
	}
	xhttp.onerror = function (e) {
	    var data = '{"Response":"Success","Type":100,"Aggregated":false,"TimeTo":1605571200,"TimeFrom":1602979200,"FirstValueInArray":true,"ConversionType":{"type":"direct","conversionSymbol":""},"Data":[{"time":1602979200,"high":11513.68,"low":11357.25,"open":11367.65,"volumefrom":11528.41,"volumeto":131886570.58,"close":11513.33,"conversionType":"direct","conversionSymbol":""},{"time":1603065600,"high":11821.95,"low":11417.11,"open":11513.33,"volumefrom":39224.67,"volumeto":456404609.75,"close":11756.88,"conversionType":"direct","conversionSymbol":""},{"time":1603152000,"high":12047.73,"low":11688.39,"open":11756.88,"volumefrom":48504.61,"volumeto":576128149.71,"close":11921.78,"conversionType":"direct","conversionSymbol":""},{"time":1603238400,"high":13236.39,"low":11900.51,"open":11921.78,"volumefrom":103080.18,"volumeto":1296152945.69,"close":12813.11,"conversionType":"direct","conversionSymbol":""},{"time":1603324800,"high":13197.69,"low":12700.74,"open":12813.11,"volumefrom":57124.85,"volumeto":739591002.3,"close":12990.25,"conversionType":"direct","conversionSymbol":""},{"time":1603411200,"high":13031.82,"low":12732.62,"open":12990.25,"volumefrom":32269.84,"volumeto":416662855.54,"close":12937.2,"conversionType":"direct","conversionSymbol":""},{"time":1603497600,"high":13167.31,"low":12886.47,"open":12937.2,"volumefrom":20932.05,"volumeto":273005904.67,"close":13126.13,"conversionType":"direct","conversionSymbol":""},{"time":1603584000,"high":13346.7,"low":12910.39,"open":13126.13,"volumefrom":28208.48,"volumeto":368884232.62,"close":13041.21,"conversionType":"direct","conversionSymbol":""},{"time":1603670400,"high":13241.79,"low":12797.05,"open":13041.21,"volumefrom":35322.99,"volumeto":460984686.3,"close":13069.43,"conversionType":"direct","conversionSymbol":""},{"time":1603756800,"high":13783.14,"low":13060.64,"open":13069.43,"volumefrom":44978.37,"volumeto":603406480.39,"close":13646.02,"conversionType":"direct","conversionSymbol":""},{"time":1603843200,"high":13855.57,"low":12906.15,"open":13646.02,"volumefrom":32501.89,"volumeto":434942187.78,"close":13285.97,"conversionType":"direct","conversionSymbol":""},{"time":1603929600,"high":13643.6,"low":12985.56,"open":13285.97,"volumefrom":41497.54,"volumeto":555737562.11,"close":13462.18,"conversionType":"direct","conversionSymbol":""},{"time":1604016000,"high":13674.89,"low":13132.53,"open":13462.18,"volumefrom":56364.21,"volumeto":756044940.71,"close":13565.95,"conversionType":"direct","conversionSymbol":""},{"time":1604102400,"high":14077.8,"low":13432.24,"open":13565.95,"volumefrom":43579.77,"volumeto":600104833.89,"close":13803.41,"conversionType":"direct","conversionSymbol":""},{"time":1604188800,"high":13897.02,"low":13630.22,"open":13803.41,"volumefrom":20841.63,"volumeto":286724152.06,"close":13761.72,"conversionType":"direct","conversionSymbol":""},{"time":1604275200,"high":13828.48,"low":13221.65,"open":13761.72,"volumefrom":33465.17,"volumeto":453096297.52,"close":13571.24,"conversionType":"direct","conversionSymbol":""},{"time":1604361600,"high":14071.54,"low":13300.84,"open":13571.24,"volumefrom":21969.7,"volumeto":300271386.78,"close":14023.78,"conversionType":"direct","conversionSymbol":""},{"time":1604448000,"high":14258.9,"low":13539.13,"open":14023.78,"volumefrom":30406.02,"volumeto":423118194.37,"close":14157.73,"conversionType":"direct","conversionSymbol":""},{"time":1604534400,"high":15739.47,"low":14114.37,"open":14157.73,"volumefrom":42121.25,"volumeto":625288741.44,"close":15599.92,"conversionType":"direct","conversionSymbol":""},{"time":1604620800,"high":15948.88,"low":15219.57,"open":15599.92,"volumefrom":34543.56,"volumeto":538014394.46,"close":15590.62,"conversionType":"direct","conversionSymbol":""},{"time":1604707200,"high":15765.02,"low":14427.34,"open":15590.62,"volumefrom":25695.27,"volumeto":388303730.2,"close":14838.16,"conversionType":"direct","conversionSymbol":""},{"time":1604793600,"high":15653.89,"low":14739.11,"open":14838.16,"volumefrom":18706.65,"volumeto":285202500.11,"close":15488.25,"conversionType":"direct","conversionSymbol":""},{"time":1604880000,"high":15812.23,"low":14833.13,"open":15488.25,"volumefrom":32088.79,"volumeto":492570531.42,"close":15335.03,"conversionType":"direct","conversionSymbol":""},{"time":1604966400,"high":15476.99,"low":15099.11,"open":15335.03,"volumefrom":23031.66,"volumeto":352628988.82,"close":15313.73,"conversionType":"direct","conversionSymbol":""},{"time":1605052800,"high":15983.03,"low":15288.76,"open":15313.73,"volumefrom":45852.83,"volumeto":717920492.19,"close":15707.08,"conversionType":"direct","conversionSymbol":""},{"time":1605139200,"high":16348.99,"low":15476.25,"open":15707.08,"volumefrom":67322.57,"volumeto":1074746061.94,"close":16306.53,"conversionType":"direct","conversionSymbol":""},{"time":1605225600,"high":16482.62,"low":15975.8,"open":16306.53,"volumefrom":42676.28,"volumeto":694320640.17,"close":16332.85,"conversionType":"direct","conversionSymbol":""},{"time":1605312000,"high":16334.29,"low":15720.61,"open":16332.85,"volumefrom":28331.05,"volumeto":452657737.75,"close":16075.95,"conversionType":"direct","conversionSymbol":""},{"time":1605398400,"high":16156.82,"low":15796.03,"open":16075.95,"volumefrom":17966.53,"volumeto":286912254.78,"close":15964.7,"conversionType":"direct","conversionSymbol":""},{"time":1605484800,"high":16876.48,"low":15877.77,"open":15964.7,"volumefrom":41641.22,"volumeto":685608661.41,"close":16721.46,"conversionType":"direct","conversionSymbol":""},{"time":1605571200,"high":17857.37,"low":16563.5,"open":16721.46,"volumefrom":44747.59,"volumeto":765629834.05,"close":17791.48,"conversionType":"direct","conversionSymbol":""}],"RateLimit":{},"HasWarning":false}';
	    handle_chart(data);
	};
	xhttp.open("GET", url, true);
	xhttp.send();
    }

    function handle_chart(data) {
	let parsed_data = JSON.parse(data);
	parsed_data = parsed_data.Data;

	$.each(parsed_data, function (index, value) {
	    dataSet.push([value.time * 1000, value.high]);
	});

	var options = {
	    series: [{
		    data: dataSet
		},
	    ],
	    chart: {
		id: 'area-datetime',
		type: 'area',
		height: 190,
		toolbar: {
		    show: false
		}
	    },
	    stroke: {
		colors: '#fff',
		width: 2,
	    },
	    dataLabels: {
		enabled: false
	    },
	    grid: {
		show: false
	    },
	    xaxis: {
		labels: {
		    show: false
		},
		axisBorder: {
		    show: false
		}
	    },
	    yaxis: {
		labels: {
		    show: false
		},
	    },
	    tooltip: {
		enabled: false,
	    },
	    fill: {
		type: 'gradient',
		colors: '#fff',
		gradient: {
		    shadeIntensity: 1,
		    inverseColors: false,
		    opacityFrom: 0.7,
		    opacityTo: 0,
		    stops: [0, 90, 100]
		}
	    },
	};


	if ($("#chart")) {
	    var chart = new ApexCharts(document.querySelector("#chart"), options);
	    chart.render();
	}
	if ($("#chart2")) {
	    var chart2 = new ApexCharts(document.querySelector("#chart2"), options);
	    chart2.render();
	}
	if ($("#chart3")) {
	    var chart3 = new ApexCharts(document.querySelector("#chart3"), options);
	    chart3.render();
	}
	if ($("#chart4")) {
	    var chart4 = new ApexCharts(document.querySelector("#chart4"), options);
	    chart4.render();
	}
	if ($("#chart5")) {
	    var chart5 = new ApexCharts(document.querySelector("#chart5"), options);
	    chart5.render();
	}
	if ($("#chart6")) {
	    var chart6 = new ApexCharts(document.querySelector("#chart6"), options);
	    chart6.render();
	}
	if ($("#chart7")) {
	    var chart7 = new ApexCharts(document.querySelector("#chart7"), options);
	    chart7.render();
	}
	if ($("#chart8")) {
	    var chart8 = new ApexCharts(document.querySelector("#chart8"), options);
	    chart8.render();
	}
	if ($("#chart9")) {
	    var chart9 = new ApexCharts(document.querySelector("#chart9"), options);
	    chart9.render();
	}
	if ($("#chart10")) {
	    var chart10 = new ApexCharts(document.querySelector("#chart10"), options);
	    chart10.render();
	}
	if ($("#chart11")) {
	    var chart11 = new ApexCharts(document.querySelector("#chart11"), options);
	    chart11.render();
	}
	if ($("#chart12")) {
	    var chart12 = new ApexCharts(document.querySelector("#chart12"), options);
	    chart12.render();
	}
	if ($("#chart13")) {
	    var chart13 = new ApexCharts(document.querySelector("#chart13"), options);
	    chart13.render();
	}
	if ($("#chart14")) {
	    var chart14 = new ApexCharts(document.querySelector("#chart14"), options);
	    chart14.render();
	}
	if ($("#chart15")) {
	    var chart15 = new ApexCharts(document.querySelector("#chart15"), options);
	    chart15.render();
	}
	if ($("#chart16")) {
	    var chart16 = new ApexCharts(document.querySelector("#chart16"), options);
	    chart16.render();
	}
    }

    ajax_request(ajaxUrl);

})(jQuery);