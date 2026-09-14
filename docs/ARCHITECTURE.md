# AtariStudio architecture

AtariStudio is the Atari-specific RetroStudio product/backend. RetroStudio owns generic project/editor/toolchain concepts; AtariStudio owns Atari machine knowledge.

## Dependency rule

AtariStudio may depend on RetroStudio. RetroStudio must never depend on AtariStudio.

## AtariStudio responsibilities

- target profiles for ST, STE, TT and Falcon;
- Atari-specific graphics and audio conversion;
- machine capability and resource validation;
- Atari runtime/toolchain integration;
- disk/executable packaging;
- emulator launch and qualification workflows;
- hardware-aware diagnostics.

## RetroStudio responsibilities

- project/scene/entity models;
- shared asset source model;
- scripting/event interfaces;
- generic build graph;
- Linux editor infrastructure;
- backend discovery and diagnostics contracts;
- host preview abstractions.

## Initial target families

### Atari ST

68000 compatibility baseline. Initial profiles should cover classic ST constraints without assuming STE-only hardware.

### Atari STE

68000 family with enhanced graphics/audio capabilities. STE extensions must be capability flags, not implicit defaults.

### Atari TT

68030-class target with its own video/memory characteristics.

### Atari Falcon

68030-class target with VIDEL/DSP-era capabilities. Falcon support must remain an explicit target so the ST baseline is not polluted by later-machine assumptions.

## Emulator strategy

Hatari is the primary emulator integration target for ST/STE/TT/Falcon workflows. Emulator integration is outside the RetroStudio core.

## M0 non-goals

- production runtime;
- image/audio conversion;
- executable or disk-image production;
- TOS/ROM handling;
- emulator automation;
- graphical editor implementation.

M0 establishes boundaries and testable repository structure only.
