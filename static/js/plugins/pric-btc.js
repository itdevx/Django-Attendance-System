(function ($) {
    let ajaxUrl = "https://min-api.cryptocompare.com/data/histoday?fsym=BTC&tsym=USD&limit=30";
    let dataSet = [];

    function ajax_request(url) {
	let xhttp;
	xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function () {
	    if (this.readyState == 4 && this.status == 200) {
		handle_chart(this);
	    }
	}
	xhttp.open("GET", url, true);
	xhttp.send();
    }

    function handle_chart(data) {
	let parsed_data = JSON.parse(data.responseText);
	parsed_data = parsed_data.Data;

	$.each(parsed_data, function (index, value) {
	    dataSet.push([value.time * 1000, value.high]);
	});

	let options = {
	    chart: {
		id: 'area-datetime',
		type: 'area',
		height: 350,
		toolbar: {
		    show: false
		},
		fontFamily: 'IRANYekan',
	    },
	    stroke: {
		colors: '#F7931A',
		width: 10,
	    },
	    dataLabels: {
		enabled: false
	    },
	    grid: {
		show: false,
		borderColor: '#F1F1F1',
	    },
	    tooltip: {
		x: {
		    format: "dd MMM yyyy"
		},
		fixed: {
		    enabled: false,
		    position: 'topRight'
		}
	    },

	    fill: {
		type: 'gradient',
		colors: '#2F2CD8',
		gradient: {
		    shadeIntensity: 1,
		    opacityFrom: 0.5,
		    opacityTo: 1,
		    stops: [0, 100]
		}
	    },
	    colors: ['#F8CCCD'],
	    series: [{
		    name: 'BTC (USD)',
		    data: dataSet
		},
	    ],
	    xaxis: {
		labels: {
		    show: false
		},
	    },
	    yaxis: {
		labels: {
		    show: false
		},
	    },
	};
	let chart = new ApexCharts(document.querySelector("#btcChart"), options);
	chart.render();
    }

    $(window).on('load', function () {
	setTimeout(function () {
	    $('.loader').fadeOut();
	    $('#timeline-chart').addClass('loaded');
	}, 1200);
    });

    ajax_request(ajaxUrl);




})(jQuery);

