<template>
  <svg
    class="hero-svg"
    viewBox="0 0 420 500"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
  >
    <!-- Abstract tech line-art: nodes + connecting lines + a person silhouette suggestion -->
    <!-- Grid dots -->
    <g opacity="0.25">
      <circle cx="20" cy="60" r="2" fill="#0A0A0A"/>
      <circle cx="80" cy="60" r="2" fill="#0A0A0A"/>
      <circle cx="140" cy="60" r="2" fill="#0A0A0A"/>
      <circle cx="200" cy="60" r="2" fill="#0A0A0A"/>
      <circle cx="260" cy="60" r="2" fill="#0A0A0A"/>
      <circle cx="320" cy="60" r="2" fill="#0A0A0A"/>
      <circle cx="380" cy="60" r="2" fill="#0A0A0A"/>
      <circle cx="20" cy="120" r="2" fill="#0A0A0A"/>
      <circle cx="80" cy="120" r="2" fill="#0A0A0A"/>
      <circle cx="140" cy="120" r="2" fill="#0A0A0A"/>
      <circle cx="200" cy="120" r="2" fill="#0A0A0A"/>
      <circle cx="260" cy="120" r="2" fill="#0A0A0A"/>
      <circle cx="320" cy="120" r="2" fill="#0A0A0A"/>
      <circle cx="380" cy="120" r="2" fill="#0A0A0A"/>
      <circle cx="20" cy="180" r="2" fill="#0A0A0A"/>
      <circle cx="80" cy="180" r="2" fill="#0A0A0A"/>
      <circle cx="140" cy="180" r="2" fill="#0A0A0A"/>
      <circle cx="200" cy="180" r="2" fill="#0A0A0A"/>
      <circle cx="260" cy="180" r="2" fill="#0A0A0A"/>
      <circle cx="320" cy="180" r="2" fill="#0A0A0A"/>
      <circle cx="380" cy="180" r="2" fill="#0A0A0A"/>
    </g>

    <!-- Network graph nodes -->
    <circle cx="210" cy="200" r="8" stroke="#0A0A0A" stroke-width="1.5"/>
    <circle cx="120" cy="280" r="5" stroke="#0A0A0A" stroke-width="1.5"/>
    <circle cx="300" cy="260" r="5" stroke="#0A0A0A" stroke-width="1.5"/>
    <circle cx="170" cy="360" r="5" stroke="#0A0A0A" stroke-width="1.5"/>
    <circle cx="340" cy="340" r="5" stroke="#0A0A0A" stroke-width="1.5"/>
    <circle cx="60"  cy="340" r="3" stroke="#0A0A0A" stroke-width="1.5"/>
    <circle cx="260" cy="420" r="3" stroke="#0A0A0A" stroke-width="1.5"/>
    <circle cx="380" cy="420" r="3" stroke="#0A0A0A" stroke-width="1.5"/>

    <!-- Network edges -->
    <line x1="210" y1="200" x2="120" y2="280" stroke="#0A0A0A" stroke-width="1" stroke-dasharray="4 4" opacity="0.5"/>
    <line x1="210" y1="200" x2="300" y2="260" stroke="#0A0A0A" stroke-width="1" stroke-dasharray="4 4" opacity="0.5"/>
    <line x1="120"  y1="280" x2="170" y2="360" stroke="#0A0A0A" stroke-width="1" opacity="0.4"/>
    <line x1="120"  y1="280" x2="60"  y2="340" stroke="#0A0A0A" stroke-width="1" opacity="0.4"/>
    <line x1="300" y1="260" x2="340" y2="340" stroke="#0A0A0A" stroke-width="1" opacity="0.4"/>
    <line x1="170" y1="360" x2="260" y2="420" stroke="#0A0A0A" stroke-width="1" opacity="0.35"/>
    <line x1="340" y1="340" x2="380" y2="420" stroke="#0A0A0A" stroke-width="1" opacity="0.35"/>
    <line x1="300" y1="260" x2="170" y2="360" stroke="#0A0A0A" stroke-width="1" stroke-dasharray="3 6" opacity="0.3"/>

    <!-- Abstract arc / data flow curve -->
    <path d="M 40 460 Q 200 300 380 200" stroke="#0A0A0A" stroke-width="1" opacity="0.15" fill="none"/>
    <path d="M 40 480 Q 210 320 400 220" stroke="#0A0A0A" stroke-width="1" opacity="0.1" fill="none"/>

    <!-- Large decorative circle (niji style) -->
    <circle cx="320" cy="120" r="100" stroke="#0A0A0A" stroke-width="1" opacity="0.07"/>
    <circle cx="320" cy="120" r="70"  stroke="#0A0A0A" stroke-width="1" opacity="0.05"/>

    <!-- Bracket / code symbol -->
    <path d="M 50 90 L 30 110 L 50 130" stroke="#0A0A0A" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" opacity="0.5" fill="none"/>
    <path d="M 80 90 L 100 110 L 80 130" stroke="#0A0A0A" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" opacity="0.5" fill="none"/>

    <!-- Sine wave at bottom -->
    <path d="M0 480 C 50 460, 80 500, 130 480 S 210 460, 260 480 S 340 500, 390 480 S 430 460, 440 480"
          stroke="#0A0A0A" stroke-width="1" opacity="0.12" fill="none"/>
  </svg>
</template>

<style scoped>
.hero-svg {
  width: 100%;
  max-width: 420px;
  height: auto;
}
</style>
