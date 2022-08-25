(function ($) {
    var options = {
	series: [44, 55, 13, 33],
	chart: {
	    height: 220,
	    type: 'donut',
	    fontFamily: 'IRANYekan',
	},
	dataLabels: {
	    enabled: false
	},
	labels: ['بیت کوین', 'تتر', 'تزوس', 'مونرو'],
	fill: {
	    colors: ['#F7931A', '#2CA07A', '#A6DF00', '#FF6600']
	},
	responsive: [{
		breakpoint: 480,
		options: {
		    chart: {
			width: 200
		    },
		    legend: {
			show: false
		    }
		}
	    }],
	legend: {
	    show: false,
	    position: 'left',
	    offsetY: 0,
	    height: 150,
	}
    };


    var chart = new ApexCharts(document.querySelector("#balance-chart"), options);
    chart.render();

})(jQuery);





// ////

(function ($) {
    $('#report-select').on('change', function () {
	drawChart();
    });

    function getSeries() {
	var selected_series = $('#report-select').val();
	if (selected_series == "1") {
	    return series1();
	}
	if (selected_series == "2") {
	    return series2();
	}
    }

    function series1() {
	var asd = [{
		name: "بیت کوین",
		data: [1698543, 1698543, 1698043, 1698143, 1698343, 1698543, 1698543, 1698443, 1698543]
	    }]
	return asd
    }

    function series2() {
	var qwe = [{
		name: "تتر",
		data: [20, 50, 90, 195, 49, 62, 69, 91, 148]
	    }]
	return qwe
    }

    var options = {
	series: getSeries(),
	chart: {
	    fontFamily: 'IRANYekan',
	    height: 300,
	    type: "area",
	    animations: {
		enabled: false
	    },
	    toolbar: {
		show: false
	    },
	},
	colors: ["#2F2CD8"],
	dataLabels: {
	    enabled: false
	},
	grid: {
	    show: false,
	    borderColor: '#F1F1F1',
	},
	xaxis: {
	    categories: ['19 آبان', '20 آبان', '21 آبان', '22 آبان', '23 آبان', '24 آبان', '25 آبان', '26 آبان', '27 آبان'],
	    axisBorder: {
		show: false
	    },
	},

    };
    if ($('#chartx').length) {
	var chart = new ApexCharts(document.querySelector("#chartx"), options);
	chart.render();

	function drawChart() {
	    chart.updateSeries(getSeries())
	}
    }

})(jQuery);