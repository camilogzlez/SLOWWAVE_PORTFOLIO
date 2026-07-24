<template>
  <div style="position: fixed; left: 50%; right: 0; top: 0; bottom: 0; background: #FAFAFA; pointer-events: none; overflow: hidden; z-index: 0;">
        <svg viewBox="0 0 700 900" style="position: absolute; inset: 0; width: 100%; height: 100%; overflow: visible;" preserveAspectRatio="xMidYMid meet">
          <circle v-for="(d, i) in dotGrid" :key="'dot' + i" :cx="d.x" :cy="d.y" r="2" fill="#ccc"></circle>

          <g :style="ringGroupStyle">
            <circle cx="560" cy="220" r="150" fill="none" stroke="#ddd" stroke-width="1"></circle>
            <circle cx="560" cy="220" r="95" fill="none" stroke="#ddd" stroke-width="1"></circle>
            <path d="M470,220 L500,220 M470,220 L485,208 M470,220 L485,232" stroke="#ccc" stroke-width="1.2" fill="none"></path>
            <path d="M650,220 L620,220 M650,220 L635,208 M650,220 L635,232" stroke="#ccc" stroke-width="1.2" fill="none"></path>
          </g>

          <g opacity="0.22">
            <path d="M480,60 L520,90 L560,72 L600,100 L640,80" fill="none" stroke="#999" stroke-width="1" stroke-dasharray="3 4"></path>
            <rect x="475" y="55" width="8" height="8" fill="none" stroke="#999" stroke-width="1"></rect>
            <rect x="635" y="75" width="8" height="8" fill="none" stroke="#999" stroke-width="1"></rect>
          </g>

          <g :style="calmStyle">
            <path d="M20,480 C110,460 160,500 250,480 C340,460 390,500 480,480 C570,460 610,500 680,480" fill="none" stroke="#bbb" stroke-width="1.4"></path>
            <path d="M20,530 C110,510 160,550 250,530 C340,510 390,550 480,530 C570,510 610,550 680,530" fill="none" stroke="#111" stroke-width="1.7"></path>
            <path d="M20,580 C110,565 160,595 250,580 C340,565 390,595 480,580 C570,565 610,595 680,580" fill="none" stroke="#ccc" stroke-width="1.2"></path>
            <g :style="fishStyle">
              <path d="M104,510 Q114,504 122,510 Q114,516 104,510 M122,510 L127,507 L127,513 Z" fill="none" stroke="#111" stroke-width="1.1"></path>
              <path d="M244,480 Q254,474 262,480 Q254,486 244,480 M262,480 L267,477 L267,483 Z" fill="none" stroke="#111" stroke-width="1.1"></path>
              <path d="M384,500 Q394,494 402,500 Q394,506 384,500 M402,500 L407,497 L407,503 Z" fill="none" stroke="#111" stroke-width="1.1"></path>
              <path d="M474,480 Q484,474 492,480 Q484,486 474,480 M492,480 L497,477 L497,483 Z" fill="none" stroke="#111" stroke-width="1.1"></path>
              <path d="M604,500 Q614,494 622,500 Q614,506 604,500 M622,500 L627,497 L627,503 Z" fill="none" stroke="#111" stroke-width="1.1"></path>
            </g>
            <g :style="dotsStyle">
              <circle cx="110" cy="510" r="3" fill="none" stroke="#111" stroke-width="1.2"></circle>
              <circle cx="250" cy="480" r="3" fill="none" stroke="#111" stroke-width="1.2"></circle>
              <circle cx="390" cy="500" r="3" fill="none" stroke="#111" stroke-width="1.2"></circle>
              <circle cx="480" cy="480" r="3" fill="none" stroke="#111" stroke-width="1.2"></circle>
              <circle cx="610" cy="500" r="3" fill="none" stroke="#111" stroke-width="1.2"></circle>
            </g>
          </g>

          <g :style="barStyle">
            <rect v-for="(bar, i) in bars" :key="'bar' + i" :x="bar.x" :y="bar.y" width="18" :height="bar.h" fill="none" stroke="#111" stroke-width="1.3" :style="bar.style"></rect>
          </g>

          <g :style="surfStyle">
            <path d="M20,600 C140,580 220,640 340,610 C460,585 520,640 640,610" fill="none" stroke="#bbb" stroke-width="1.4"></path>
            <path d="M20,520 C140,520 160,420 280,430 C400,440 420,560 320,600 C260,624 210,600 210,560" fill="none" stroke="#111" stroke-width="1.9"></path>
          </g>
          <g :style="surferStyle" :transform="surferTransform">
            <line x1="-24" y1="6" x2="24" y2="-2" stroke="#111" stroke-width="2"></line>
            <line x1="0" y1="-2" x2="0" y2="-30" stroke="#111" stroke-width="1.6"></line>
            <circle cx="0" cy="-38" r="5" fill="none" stroke="#111" stroke-width="1.6"></circle>
            <line x1="0" y1="-20" x2="-15" y2="-28" stroke="#111" stroke-width="1.6"></line>
            <line x1="0" y1="-20" x2="15" y2="-14" stroke="#111" stroke-width="1.6"></line>
            <line x1="0" y1="-6" x2="-11" y2="3" stroke="#111" stroke-width="1.6"></line>
            <line x1="0" y1="-6" x2="11" y2="0" stroke="#111" stroke-width="1.6"></line>
          </g>

          <g :style="graphStyle">
            <path d="M40,720 L110,640 L150,700 L190,560 L220,650 L260,380 L300,520 L340,460 L380,600 L430,500 L480,650 L540,560 L600,680 L660,720" fill="none" stroke="#111" stroke-width="1.6"></path>
            <path d="M40,760 L110,680 L150,740 L190,600 L220,690 L260,420 L300,560 L340,500 L380,640 L430,540 L480,690 L540,600 L600,720 L660,760" fill="none" stroke="#bbb" stroke-width="1.1" stroke-dasharray="4 4"></path>
            <circle cx="110" cy="640" r="5" fill="#fff" stroke="#111" stroke-width="1.5"></circle>
            <circle cx="190" cy="560" r="5" fill="#fff" stroke="#111" stroke-width="1.5"></circle>
            <circle cx="260" cy="380" r="5" fill="#fff" stroke="#111" stroke-width="1.5"></circle>
            <circle cx="340" cy="460" r="5" fill="#fff" stroke="#111" stroke-width="1.5"></circle>
            <circle cx="430" cy="500" r="5" fill="#fff" stroke="#111" stroke-width="1.5"></circle>
            <circle cx="540" cy="560" r="5" fill="#fff" stroke="#111" stroke-width="1.5"></circle>
            <path d="M40,800 L660,800" stroke="#ddd" stroke-width="1"></path>
          </g>

          <g :style="mountainStyle">
            <path d="M566,258 A26,26 0 1 0 566,310 A20,26 0 1 1 566,258 Z" fill="none" stroke="#111" stroke-width="1.5"></path>
            <path v-for="(star, i) in stars" :key="'star' + i" :d="star.d" fill="#111" :style="star.style"></path>
            <path d="M40,720 L110,640 L150,700 L190,560 L220,650 L260,380 L300,520 L340,460 L380,600 L430,500 L480,650 L540,560 L600,680 L660,720" fill="none" stroke="#111" stroke-width="1.8"></path>
            <path d="M40,760 L660,760" stroke="#ddd" stroke-width="1" stroke-dasharray="2 5"></path>
            <g :style="bikeStyle" :transform="bikeTransform">
              <circle cx="0" cy="30" r="16" fill="none" stroke="#111" stroke-width="1.4"></circle>
              <circle cx="56" cy="30" r="16" fill="none" stroke="#111" stroke-width="1.4"></circle>
              <path d="M0,30 L28,4 L56,30 M28,4 L28,-10 M16,-10 L40,-10 M0,30 L28,10 L56,30" fill="none" stroke="#111" stroke-width="1.4"></path>
            </g>
          </g>
        </svg>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue';

function smooth(p, a, b) {
  if (p <= a) return 0;
  if (p >= b) return 1;
  return (p - a) / (b - a);
}

const progress = ref(0);
const now = ref(Date.now());
const t0 = Date.now();

let ticking = false;
function updateProgress() {
  const scrollY = window.scrollY;
  const total = document.documentElement.scrollHeight - window.innerHeight;
  let p = total > 0 ? scrollY / total : 0;
  p = Math.max(0, Math.min(1, p));
  if (Math.abs(p - progress.value) > 0.001) progress.value = p;
}
function onScroll() {
  if (ticking) return;
  ticking = true;
  requestAnimationFrame(() => { updateProgress(); ticking = false; });
}

let twinkleInterval;
onMounted(() => {
  window.addEventListener('scroll', onScroll, { passive: true });
  updateProgress();
  twinkleInterval = setInterval(() => { now.value = Date.now(); }, 200);
});
onUnmounted(() => {
  window.removeEventListener('scroll', onScroll);
  clearInterval(twinkleInterval);
});

const dotGrid = (() => {
  const arr = [];
  for (let row = 0; row < 5; row++) {
    for (let col = 0; col < 6; col++) {
      arr.push({ x: 240 + col * 80, y: 60 + row * 60 });
    }
  }
  return arr;
})();

const barTops = [
  { x: 20, y: 520 }, { x: 74, y: 490 }, { x: 128, y: 460 }, { x: 180, y: 445 },
  { x: 230, y: 448 }, { x: 280, y: 452 }, { x: 330, y: 490 }, { x: 380, y: 560 },
];
const barBase = 610;

const starSeeds = [
  { x: 120, y: 400, s: 7, d: 2.1 }, { x: 200, y: 460, s: 5.2, d: 1.4 },
  { x: 260, y: 380, s: 6.4, d: 2.6 }, { x: 330, y: 500, s: 4.8, d: 1.8 },
  { x: 420, y: 420, s: 5.8, d: 2.2 }, { x: 480, y: 350, s: 6.6, d: 1.6 },
  { x: 540, y: 480, s: 5.2, d: 2.4 }, { x: 600, y: 400, s: 6, d: 1.2 },
  { x: 640, y: 480, s: 4.8, d: 2.8 }, { x: 70, y: 470, s: 5.4, d: 1.9 },
  { x: 380, y: 340, s: 4.8, d: 2.3 }, { x: 250, y: 440, s: 6, d: 1.5 },
  { x: 560, y: 350, s: 5.2, d: 2.0 }, { x: 160, y: 350, s: 6.4, d: 1.3 },
];

const p = computed(() => progress.value);
const scaleFor = (o) => 0.96 + 0.04 * o;

const calmClip = computed(() => `inset(0 0 0 ${smooth(p.value, 0.14, 0.22) * 100}%)`);
const barIn = computed(() => smooth(p.value, 0.14, 0.22));
const barOut = computed(() => smooth(p.value, 0.30, 0.38));
const barClip = computed(() => `inset(0 ${(1 - barIn.value) * 100}% 0 ${barOut.value * 100}%)`);
const barOpacity = computed(() => barIn.value * (1 - barOut.value));
const surfClip = computed(() => `inset(0 ${(1 - smooth(p.value, 0.30, 0.38)) * 100}% 0 ${smooth(p.value, 0.55, 0.70) * 100}%)`);
const surfVisible = computed(() => smooth(p.value, 0.30, 0.38) * (1 - smooth(p.value, 0.55, 0.70)));

const barStagger = computed(() => smooth(p.value, 0.14, 0.30));
const bars = computed(() => barTops.map((b, i) => {
  const start = i / barTops.length;
  const on = smooth(barStagger.value, start, start + 0.14);
  return { x: b.x, y: b.y, h: barBase - b.y, style: `opacity: ${on};` };
}));

const surferOpacity = computed(() => surfVisible.value * smooth(p.value, 0.34, 0.40) * (1 - smooth(p.value, 0.48, 0.52)));
const surferT = computed(() => smooth(p.value, 0.30, 0.52));
const surferX = computed(() => 120 + surferT.value * 400);
const surferTransform = computed(() => `translate(${surferX.value},640) rotate(4)`);

const mountainT = computed(() => smooth(p.value, 0.86, 1));
const bikeX = computed(() => 40 + mountainT.value * 480);
const mountainOpacity = computed(() => smooth(p.value, 0.88, 0.98));

const stars = computed(() => {
  const n = now.value;
  return starSeeds.map((st) => {
    const tw = 0.55 + 0.45 * Math.sin((n - t0) / 1000 * (Math.PI / st.d) + st.x);
    const r = st.s;
    const d = `M${st.x},${st.y - r} L${st.x + r * 0.3},${st.y - r * 0.3} L${st.x + r},${st.y} L${st.x + r * 0.3},${st.y + r * 0.3} L${st.x},${st.y + r} L${st.x - r * 0.3},${st.y + r * 0.3} L${st.x - r},${st.y} L${st.x - r * 0.3},${st.y - r * 0.3} Z`;
    return { d, style: `opacity: ${tw * mountainOpacity.value};` };
  });
});

const graphClip = computed(() => `inset(0 ${(1 - smooth(p.value, 0.55, 0.70)) * 100}% 0 0)`);
const graphOpacity = computed(() => smooth(p.value, 0.55, 0.70) * (1 - mountainOpacity.value));

const ringGroupStyle = computed(() => `transform-origin: 560px 220px; transform: rotate(${p.value * 220}deg); opacity: 0.5;`);
const calmStyle = computed(() => `clip-path: ${calmClip.value};`);
const dotsStyle = computed(() => `opacity: ${1 - smooth(p.value, 0.02, 0.09)};`);
const fishStyle = computed(() => `opacity: ${smooth(p.value, 0.05, 0.12)};`);
const barStyle = computed(() => `clip-path: ${barClip.value}; opacity: ${barOpacity.value};`);
const surfStyle = computed(() => `clip-path: ${surfClip.value};`);
const bikeStyle = computed(() => `opacity: ${mountainOpacity.value};`);
const bikeTransform = computed(() => `translate(${bikeX.value},700)`);
const surferStyle = computed(() => `opacity: ${surferOpacity.value};`);
const graphStyle = computed(() => `clip-path: ${graphClip.value}; opacity: ${graphOpacity.value};`);
const mountainStyle = computed(() => `opacity: ${mountainOpacity.value};`);
</script>
