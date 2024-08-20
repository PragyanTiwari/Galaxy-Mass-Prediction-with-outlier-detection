
# 🌌 Galaxy Mass Prediction

/* From Uiverse.io by Praashoo7 */ 
.main {
  align-items: center;
  justify-content: center;
  transform: translate(0%,25%);
}

button {
  width: 13em;
  height: 3.5em;
  border: none;
  display: flex;
  align-items: center;
  background-color: #171717;
  border-radius: 15px;
  padding-left: 1em;
  z-index: 3;
  overflow: hidden;
  transition: .4s ease-in-out;
}

.text {
  color: white;
  padding-left: 0.5em;
  padding-top: 0.1em;
  letter-spacing: 0.8em;
  transition: .4s ease-in-out;
  z-index: 3;
  font-weight: bold;
}

.planet {
  position: relative;
  margin-left: -9.55em;
  left: 2.6em;
  scale: 4;
  transition: .4s ease-in-out;
}

.img {
  margin-left: -7.25em;
  margin-top: 6.3em;
  transition: .4s ease-in-out;
  z-index: -2;
}

.img .stars {
  margin-right: -0.8em;
  margin-top: 7em;
  scale: 0.85;
  opacity: 0;
  transition: .4s ease-in-out;
}

.img .astronaut {
  position: relative;
  top: -6.2em;
  left: .65em;
}

.satalite {
  position: relative;
  left: -1em;
  top: -3em;
  animation: 4s around infinite;
  transition: .4s ease-in-out;
}

@keyframes around {
  0% {
    z-index: 5;
    transform: translateY(-3.5em) translateX(8.5em);
  }

  50% {
    transform: translateX(1em) translateY(3.5em);
  }

  100% {
    transform: translateY(-3.5em) translateX(8.5em);
    z-index: -2;
  }
}

button:hover .img {
  margin-top: -1em;
  z-index: 4;
}

button:hover .text {
  opacity: 0;
}

button:hover .planet {
  opacity: 0;
}

button:hover + .satalite {
  opacity: 0;
}

button:active {
  transform: scale(0.9);
}

button:active .stars {
  opacity: 1;
}