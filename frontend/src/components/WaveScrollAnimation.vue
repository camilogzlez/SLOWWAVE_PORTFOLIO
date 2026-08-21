<template>
  <div style="position: fixed; left: 50%; right: 0; top: 0; bottom: 0; background: #FAFAFA; pointer-events: none; overflow: hidden; z-index: 0;">
        <svg ref="svgRef" viewBox="0 0 700 900" style="position: absolute; inset: 0; width: 100%; height: 100%; overflow: visible;" preserveAspectRatio="xMidYMid meet">
          <g :style="heroPhaseStyle" :transform="`translate(0, ${heroContentShiftY})`">
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
          </g>

          <g :style="aboutPhaseStyle">
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
          </g>
        </svg>
  </div>

  <div
    v-for="(ob, i) in obstacleStates"
    :key="'obstacle' + i"
    style="position: fixed; left: 0; top: 0; width: 70px; height: 60px; pointer-events: none; overflow: visible; z-index: 0;"
    :style="ob.wrapStyle"
  >
    <svg viewBox="-10 -12 70 60" width="70" height="60" style="overflow: visible;">
      <template v-if="ob.type === 'mountain'">
        <path d="M0,40 L16,8 L24,20 L34,-2 L48,40 Z" fill="none" stroke="#b5b5b5" stroke-width="1.3"></path>
      </template>
      <template v-else-if="ob.type === 'city'">
        <rect x="0" y="18" width="9" height="22" fill="none" stroke="#b5b5b5" stroke-width="1.2"></rect>
        <rect x="12" y="6" width="9" height="34" fill="none" stroke="#b5b5b5" stroke-width="1.2"></rect>
        <rect x="24" y="14" width="9" height="26" fill="none" stroke="#b5b5b5" stroke-width="1.2"></rect>
        <rect x="36" y="-2" width="9" height="42" fill="none" stroke="#b5b5b5" stroke-width="1.2"></rect>
        <path d="M-4,40 L50,40" stroke="#ddd" stroke-width="1" stroke-dasharray="2 4"></path>
      </template>
      <template v-else-if="ob.type === 'skate'">
        <circle cx="20" cy="6" r="4" fill="none" stroke="#b5b5b5" stroke-width="1.2"></circle>
        <path d="M20,10 L18,22" fill="none" stroke="#b5b5b5" stroke-width="1.3"></path>
        <path d="M18,13 L28,8 M18,13 L10,18" fill="none" stroke="#b5b5b5" stroke-width="1.2"></path>
        <path d="M18,22 L10,28 M18,22 L26,26" fill="none" stroke="#b5b5b5" stroke-width="1.2"></path>
        <path d="M4,30 L32,26" fill="none" stroke="#b5b5b5" stroke-width="1.6"></path>
        <circle cx="9" cy="32" r="2" fill="none" stroke="#b5b5b5" stroke-width="1"></circle>
        <circle cx="27" cy="28" r="2" fill="none" stroke="#b5b5b5" stroke-width="1"></circle>
      </template>
      <template v-else-if="ob.type === 'wave'">
        <path d="M-6,28 C2,20 8,36 16,28 C24,20 30,36 38,28 C46,20 52,36 58,28" fill="none" stroke="#b5b5b5" stroke-width="1.4"></path>
        <path d="M-6,36 C2,30 8,42 16,36 C24,30 30,42 38,36" fill="none" stroke="#ccc" stroke-width="1"></path>
      </template>
      <template v-else-if="ob.type === 'cat'">
        <path d="M9,30 C9,21 13,17 18,17 C23,17 27,21 27,30" fill="none" stroke="#b5b5b5" stroke-width="1.1"></path>
        <path d="M26,28 C32,27 33,19 27,15" fill="none" stroke="#b5b5b5" stroke-width="1.1"></path>
        <circle cx="18" cy="11" r="7" fill="none" stroke="#b5b5b5" stroke-width="1.1"></circle>
        <path d="M12,6 Q10.5,-1 17,3.5" fill="none" stroke="#b5b5b5" stroke-width="1"></path>
        <path d="M24,6 Q25.5,-1 19,3.5" fill="none" stroke="#b5b5b5" stroke-width="1"></path>
        <circle cx="15.3" cy="11" r="0.8" fill="#b5b5b5"></circle>
        <circle cx="20.7" cy="11" r="0.8" fill="#b5b5b5"></circle>
        <circle cx="18" cy="13.2" r="0.55" fill="#b5b5b5"></circle>
        <path d="M16.2,14.6 Q18,16 19.8,14.6" fill="none" stroke="#b5b5b5" stroke-width="0.8"></path>
        <path d="M9.5,10.5 L13,11 M9.5,12.5 L13,12.5" fill="none" stroke="#ccc" stroke-width="0.7"></path>
        <path d="M26.5,10.5 L23,11 M26.5,12.5 L23,12.5" fill="none" stroke="#ccc" stroke-width="0.7"></path>
      </template>
    </svg>
  </div>

  <div style="position: fixed; left: 0; top: 0; width: 88px; height: 56px; pointer-events: none; overflow: visible; z-index: 0;" :style="gutterBikeWrapStyle">
    <svg viewBox="-16 -10 88 56" width="88" height="56" style="overflow: visible;">
      <circle cx="0" cy="30" r="16" fill="none" stroke="#999" stroke-width="1.4"></circle>
      <circle cx="56" cy="30" r="16" fill="none" stroke="#999" stroke-width="1.4"></circle>
      <path d="M0,30 L28,4 L56,30 M28,4 L28,-10 M16,-10 L40,-10 M0,30 L28,10 L56,30" fill="none" stroke="#999" stroke-width="1.4"></path>
    </svg>
  </div>
</template>

<script setup>
import { ref, reactive, computed, onMounted, onUnmounted } from 'vue';

function smooth(p, a, b) {
  if (p <= a) return 0;
  if (p >= b) return 1;
  return (p - a) / (b - a);
}

// triangle wave in [-1, 1], repeating `cycles` times over t in [0, 1]
function zigzag(t, cycles) {
  const x = ((t * cycles) % 1 + 1) % 1;
  return x < 0.5 ? x * 4 - 1 : 3 - x * 4;
}

const now = ref(Date.now());
const t0 = Date.now();

// section-relative scroll progress, recomputed straight from the DOM every tick
// so it self-corrects when async content (project cards) changes section heights
const state = reactive({
  heroProgress: 0,
  bikeProgress: 0,
  bikeActive: false,
  aboutProgress: 0,
  aboutActive: false,
});

const gutterX = ref(0);
const gutterY = ref(0);
const gutterOpacity = ref(0);
const gutterMidX = ref(0);
const gutterHalfW = ref(0);
const gutterViewportH = ref(0);
const GUTTER_TOP_PAD = 60;
const GUTTER_BOTTOM_PAD = 100;

// small scenery the bike passes on its way down the gutter. `side` is picked
// opposite of where the bike's own zigzag puts it at that same progress, so
// the icon sits beside the path instead of colliding with the bike.
const OBSTACLES = [
  { type: 'mountain', p: 0.14, side: -1 },
  { type: 'city', p: 0.36, side: -1 },
  { type: 'skate', p: 0.58, side: 1 },
  { type: 'cat', p: 0.76, side: 1 },
  { type: 'wave', p: 0.92, side: -1 },
];

// vertical translate (in SVG user-space units) applied to the whole hero
// scene so it lines up next to the first name. The hero scene is fully
// visible from page load (its "at rest" state is unclipped, it only wipes
// away once heroProgress starts advancing), so it must track "Camilo"'s
// actual live position on screen -- not a hypothetical future scroll
// position. It tracks continuously while heroProgress is still 0, then
// freezes once the scroll-driven sequence takes over.
const svgRef = ref(null);
const heroContentShiftY = ref(0);
const HERO_SCENE_ANCHOR = { x: 350, y: 520 }; // roughly the calm-water/bars/surf block's vertical center

function alignHeroSceneToName() {
  const svgEl = svgRef.value;
  const firstNameEl = document.getElementById('hero-first-name');
  if (!svgEl || !firstNameEl) return;

  const rect = firstNameEl.getBoundingClientRect();
  const targetCenterY = rect.top + rect.height / 2 + 30;

  const ctm = svgEl.getScreenCTM();
  if (!ctm) return;
  const pt = svgEl.createSVGPoint();
  pt.x = HERO_SCENE_ANCHOR.x;
  pt.y = HERO_SCENE_ANCHOR.y;
  const screenPt = pt.matrixTransform(ctm);
  const scaleY = ctm.d || 1;

  heroContentShiftY.value = (targetCenterY - screenPt.y) / scaleY;
}

let ticking = false;
function updateProgress() {
  const scrollY = window.scrollY;
  const viewportH = window.innerHeight;

  const projectsEl = document.getElementById('projects');
  const aboutEl = document.getElementById('about');
  if (!projectsEl || !aboutEl) return;

  const projRect = projectsEl.getBoundingClientRect();
  const projDocTop = projRect.top + scrollY;
  const aboutDocTop = aboutEl.getBoundingClientRect().top + scrollY;

  // hero animation: starts immediately with the very first scroll (the scene
  // is already aligned next to the name at rest, so there's no need to wait
  // for a scroll threshold), finishes just before the project cards arrive.
  const heroStart = 0;
  const heroEnd = Math.max(heroStart + viewportH * 0.5, projDocTop - 100);
  state.heroProgress = Math.max(0, Math.min(1, (scrollY - heroStart) / (heroEnd - heroStart)));

  // keep the scene glued to the name right up until the sequence triggers
  if (state.heroProgress <= 0) alignHeroSceneToName();

  // bicycle-in-the-gutter: spans the whole projects section scroll
  const bikeStart = heroEnd;
  const bikeEnd = Math.max(bikeStart + 1, aboutDocTop - viewportH);
  state.bikeProgress = Math.max(0, Math.min(1, (scrollY - bikeStart) / (bikeEnd - bikeStart)));
  state.bikeActive = scrollY >= bikeStart && scrollY < bikeEnd;

  // finale: graph -> mountains/stars/bike, resumes as the about section arrives
  const aboutStart = bikeEnd;
  const aboutFinaleSpan = viewportH * 1.2;
  state.aboutProgress = Math.max(0, Math.min(1, (scrollY - aboutStart) / aboutFinaleSpan));
  state.aboutActive = scrollY >= aboutStart;

  // measure the real gutter (space between the project cards and the viewport edge)
  const containerEl = projectsEl.querySelector('.container');
  const containerRight = containerEl ? containerEl.getBoundingClientRect().right : projRect.right;
  const gutterLeft = Math.min(containerRight, window.innerWidth - 60);
  const gutterRight = window.innerWidth;
  gutterMidX.value = (gutterLeft + gutterRight) / 2;
  gutterHalfW.value = Math.max(0, (gutterRight - gutterLeft) / 2 - 20);
  gutterViewportH.value = viewportH;

  gutterY.value = GUTTER_TOP_PAD + state.bikeProgress * Math.max(0, viewportH - GUTTER_TOP_PAD - GUTTER_BOTTOM_PAD);
  gutterX.value = gutterMidX.value + zigzag(state.bikeProgress, 4) * gutterHalfW.value;

  // bike fades in a little after entering the projects section (not immediately)
  // and fades out gray/soft before the finale takes over
  const fadeIn = smooth(state.bikeProgress, 0.08, 0.16);
  const fadeOut = 1 - smooth(state.bikeProgress, 0.96, 1);
  gutterOpacity.value = state.bikeActive ? fadeIn * fadeOut : 0;
}
function onScroll() {
  if (ticking) return;
  ticking = true;
  requestAnimationFrame(() => { updateProgress(); ticking = false; });
}
function onResize() {
  alignHeroSceneToName();
  onScroll();
}

let twinkleInterval;
onMounted(() => {
  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', onResize, { passive: true });
  alignHeroSceneToName();
  updateProgress();
  twinkleInterval = setInterval(() => { now.value = Date.now(); }, 200);
});
onUnmounted(() => {
  window.removeEventListener('scroll', onScroll);
  window.removeEventListener('resize', onResize);
  clearInterval(twinkleInterval);
});

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

// --- hero phase (dot grid -> calm water -> bar chart -> surf & surfer) ---
const heroP = computed(() => state.heroProgress);

const calmClip = computed(() => `inset(0 0 0 ${smooth(heroP.value, 0.20, 0.31) * 100}%)`);
const barIn = computed(() => smooth(heroP.value, 0.20, 0.31));
const barOut = computed(() => smooth(heroP.value, 0.43, 0.54));
const barClip = computed(() => `inset(0 ${(1 - barIn.value) * 100}% 0 ${barOut.value * 100}%)`);
const barOpacity = computed(() => barIn.value * (1 - barOut.value));
const surfClip = computed(() => `inset(0 ${(1 - smooth(heroP.value, 0.43, 0.54)) * 100}% 0 ${smooth(heroP.value, 0.79, 1.0) * 100}%)`);
const surfVisible = computed(() => smooth(heroP.value, 0.43, 0.54) * (1 - smooth(heroP.value, 0.79, 1.0)));

const barStagger = computed(() => smooth(heroP.value, 0.20, 0.43));
const bars = computed(() => barTops.map((b, i) => {
  const start = i / barTops.length;
  const on = smooth(barStagger.value, start, start + 0.14);
  return { x: b.x, y: b.y, h: barBase - b.y, style: `opacity: ${on};` };
}));

// surfer glides in and holds position through the end of the hero phase
const surferOpacity = computed(() => surfVisible.value * smooth(heroP.value, 0.49, 0.57));
const surferT = computed(() => smooth(heroP.value, 0.43, 0.74));
const surferX = computed(() => 120 + surferT.value * 400);
const surferTransform = computed(() => `translate(${surferX.value},640) rotate(4)`);

const dotsStyle = computed(() => `opacity: ${1 - smooth(heroP.value, 0.03, 0.13)};`);
const fishStyle = computed(() => `opacity: ${smooth(heroP.value, 0.07, 0.17)};`);
const barStyle = computed(() => `clip-path: ${barClip.value}; opacity: ${barOpacity.value};`);
const surfStyle = computed(() => `clip-path: ${surfClip.value};`);
const surferStyle = computed(() => `opacity: ${surferOpacity.value};`);
const calmStyle = computed(() => `clip-path: ${calmClip.value};`);
const heroPhaseStyle = computed(() => `opacity: ${state.bikeActive || state.aboutActive ? 0 : 1}; transition: opacity 0.5s ease;`);

// on narrow screens the gutter shrinks to almost nothing, so the bike/
// scenery icons (authored at a fixed pixel size) need to shrink with it or
// they overrun the space and overlap the cards.
const sceneScale = computed(() => Math.max(0.45, Math.min(1, gutterHalfW.value / 70)));

// --- gutter bicycle (projects section) ---
// wrapper div is sized to the icon itself (88x56) so `scale()` pivots around
// its own center, landing exactly on (gutterX, gutterY) at any scale.
const gutterBikeWrapStyle = computed(() => {
  const s = sceneScale.value;
  return `opacity: ${gutterOpacity.value}; transform: translate(${gutterX.value - 44}px, ${gutterY.value - 28}px) scale(${s}); transition: opacity 0.3s ease;`;
});

// --- scenery the bike passes on the way down: mountain, city, skate, cat, wave ---
const obstacleStates = computed(() => {
  const span = Math.max(0, gutterViewportH.value - GUTTER_TOP_PAD - GUTTER_BOTTOM_PAD);
  const s = sceneScale.value;
  return OBSTACLES.map((ob) => {
    // sits a bit ahead of (above) where the bike is at that same progress --
    // in a narrow gutter, horizontal separation alone isn't reliable, so the
    // vertical offset is what actually keeps it clear of the bike.
    const y = GUTTER_TOP_PAD + ob.p * span - 46;
    const x = gutterMidX.value + ob.side * gutterHalfW.value * 0.7;
    const reveal = smooth(state.bikeProgress, ob.p - 0.16, ob.p - 0.05) * (1 - smooth(state.bikeProgress, ob.p + 0.05, ob.p + 0.16));
    const opacity = state.bikeActive ? reveal * 0.7 : 0;
    return {
      type: ob.type,
      wrapStyle: `opacity: ${opacity}; transform: translate(${x - 35}px, ${y - 30}px) scale(${s}); transition: opacity 0.3s ease;`,
    };
  });
});

// --- finale (graph -> mountains, stars, bike), resumes at the about section ---
const aboutP = computed(() => state.aboutProgress);

const graphClip = computed(() => `inset(0 ${(1 - smooth(aboutP.value, 0, 0.35)) * 100}% 0 0)`);
const mountainOpacity = computed(() => smooth(aboutP.value, 0.30, 0.55));
const graphOpacity = computed(() => smooth(aboutP.value, 0, 0.35) * (1 - mountainOpacity.value));

const mountainT = computed(() => smooth(aboutP.value, 0.30, 1));
const bikeX = computed(() => 40 + mountainT.value * 480);

const stars = computed(() => {
  const n = now.value;
  return starSeeds.map((st) => {
    const tw = 0.55 + 0.45 * Math.sin((n - t0) / 1000 * (Math.PI / st.d) + st.x);
    const r = st.s;
    const d = `M${st.x},${st.y - r} L${st.x + r * 0.3},${st.y - r * 0.3} L${st.x + r},${st.y} L${st.x + r * 0.3},${st.y + r * 0.3} L${st.x},${st.y + r} L${st.x - r * 0.3},${st.y + r * 0.3} L${st.x - r},${st.y} L${st.x - r * 0.3},${st.y - r * 0.3} Z`;
    return { d, style: `opacity: ${tw * mountainOpacity.value};` };
  });
});

const bikeStyle = computed(() => `opacity: ${mountainOpacity.value};`);
const bikeTransform = computed(() => `translate(${bikeX.value},700)`);
const graphStyle = computed(() => `clip-path: ${graphClip.value}; opacity: ${graphOpacity.value};`);
const mountainStyle = computed(() => `opacity: ${mountainOpacity.value};`);
const aboutPhaseStyle = computed(() => `opacity: ${state.aboutActive ? 1 : 0}; transition: opacity 0.5s ease;`);
</script>
