//selectors
weddingLink = document.getElementById('wedding');
ringLink = document.getElementById('ring');
receptionLink = document.getElementById('reception');

container1 = document.getElementById('c1');
container2 = document.getElementById('c2');
container3 = document.getElementById('c3');

close = document.querySelector('.close');
contentContainer = document.querySelector('.content-container');

//event listeners
weddingLink.addEventListener('click', function(){
    contentContainer.style.display = 'block';
    container2.style.display='block';
    container2.style.animation='grow 0.2s ease-in';
    container1.style.display='none';
    container3.style.display='none';
});
ringLink.addEventListener('click', function(){
    contentContainer.style.display = 'block';
    container1.style.display='block';
    container1.style.animation='grow 0.2s ease-in';
    container2.style.display='none';
    container3.style.display='none';
});
receptionLink.addEventListener('click', function(){
    contentContainer.style.display = 'block';
    container3.style.display='block';
    container3.style.animation='grow 0.2s ease-in';
    container1.style.display='none';
    container2.style.display='none';
});
close.addEventListener('click', function(){
    contentContainer.style.display='none';
});

