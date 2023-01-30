//Celui qui y touche je l'abats
const img2 = document.getElementById('carousel2');
const rightBtn2 = document.getElementById('right-btn2');
const leftBtn2 = document.getElementById('left-btn2');

// Insertion d'images dans le 'let pictures' 
let pictures2 = ['images/imagebanc.png', 'images/imgruine.png'];

img2.src = pictures2[0];
let position2 = 0;

const moveRight2 = () => {
    if (position2 >= pictures2.length - 1) {
        position2 = 0
        img2.src = pictures2[position2];
        return;
    }
    img2.src = pictures2[position2 + 1];
    position2++;
}

const moveLeft2 = () => {
    if (position2 < 1) {
        position2 = pictures2.length - 1;
        img2.src = pictures2[position2];
        return;
    }
    img2.src = pictures2[position2 - 1];
    position2--;
}

rightBtn2.addEventListener("click", moveRight2);
leftBtn2.addEventListener("click", moveLeft2);