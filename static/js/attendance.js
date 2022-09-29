let status = document.getElementById('status');
let time_takhir = document.getElementById('tt');
let ghebat_movajah = document.getElementById('gm');
let ghebat_g_movajah = document.getElementById('gg');
let morkhasi = document.getElementById('mor');

time_takhir.style.display = 'none';
ghebat_movajah.style.display = 'none';
ghebat_g_movajah.style.display = 'none';
morkhasi.style.display = 'none';
   
time_takhir.labels[0].style.display = 'none';
ghebat_movajah.labels[0].style.display = 'none';
ghebat_g_movajah.labels[0].style.display = 'none';
morkhasi.labels[0].style.display = 'none';




function changeStatus(){
    if (status.value == '1'){
        time_takhir.style.display = 'none';
        ghebat_movajah.style.display = 'none';
        ghebat_g_movajah.style.display = 'none';
        morkhasi.style.display = 'none';   
    }

    else if (status.value == '2'){
        time_takhir.style.display = 'block';
        ghebat_movajah.style.display = 'none';
        ghebat_g_movajah.style.display = 'none';
        morkhasi.style.display = 'none';
        time_takhir.labels[0].style.display = 'block';
        ghebat_movajah.labels[0].style.display = 'none';
        ghebat_g_movajah.labels[0].style.display = 'none';
        morkhasi.labels[0].style.display = 'none';
        

    }
    else if (status.value == '3'){
        time_takhir.style.display = 'none';
        ghebat_movajah.style.display = 'block';
        ghebat_g_movajah.style.display = 'none';
        morkhasi.style.display = 'none';
        time_takhir.labels[0].style.display = 'none';
        ghebat_movajah.labels[0].style.display = 'none';
        ghebat_g_movajah.labels[0].style.display = 'block';
        morkhasi.labels[0].style.display = 'none';
    
        
    }
    else if (status.value == '4'){
        time_takhir.style.display = 'none';
        ghebat_movajah.style.display = 'none';
        ghebat_g_movajah.style.display = 'block';
        morkhasi.style.display = 'none';
        time_takhir.labels[0].style.display = 'none';
        ghebat_movajah.labels[0].style.display = 'block';
        ghebat_g_movajah.labels[0].style.display = 'none';
        morkhasi.labels[0].style.display = 'none';
        

    }
    else if (status.value == '5'){
        time_takhir.style.display = 'none';
        ghebat_movajah.style.display = 'none';
        ghebat_g_movajah.style.display = 'none';
        morkhasi.style.display = 'block';
        time_takhir.labels[0].style.display = 'none';
        ghebat_movajah.labels[0].style.display = 'none';
        ghebat_g_movajah.labels[0].style.display = 'none';
        morkhasi.labels[0].style.display = 'block';
    }
}