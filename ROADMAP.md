# AtariStudio roadmap

## M0 — Foundation

- [x] Define AtariStudio as an Atari-specific RetroStudio consumer/backend.
- [x] Define initial ST/STE/TT/Falcon target families.
- [x] Define dependency boundary with RetroStudio.
- [x] Add minimal target descriptor fixture.
- [x] Add host-side checks and CI.
- [x] Document hardware-aware design goals and Hatari-first emulator strategy.

Exit criterion: `make check` validates the repository, target profile data and RetroStudio API descriptor without requiring an Atari SDK, TOS image or emulator.

## M1 — Target profiles

- Machine profile parser/model.
- ST/STE/TT/Falcon capability flags.
- CPU, video, audio and memory constraints.
- PAL/NTSC/mono timing/display metadata where relevant.
- Stable diagnostics for invalid target settings.
- Tests for all baseline profiles.

## M2 — RetroStudio backend integration

- Implement RetroStudio target API negotiation.
- Backend discovery descriptor.
- Capability reporting.
- Structured target validation.
- Reference build/package hooks.

## M3 — Graphics asset pipeline

- Source bitmap ingestion handoff.
- Palette/planar conversion.
- Tiles, masks and sprite/object conversion policies.
- ST/STE/TT/Falcon constraints and diagnostics.

## M4 — Audio asset pipeline

- YM2149-oriented asset path for ST.
- STE DMA audio path.
- Falcon audio capabilities.
- Target-aware size/rate/channel diagnostics.

## M5 — 68k runtime foundation

- 68000 baseline runtime.
- 68030 TT/Falcon path.
- Input, timing, scene and entity runtime bridge.
- Deterministic runtime fixtures.

## M6 — Build and packaging

- m68k Atari cross-toolchain integration.
- Executable output.
- ST/MSA-style disk packaging path where appropriate.
- Hard-disk layout.
- Falcon/TT packaging considerations.

## M7 — Emulator workflow

- One-command build and launch.
- Hatari integration first.
- Automated guest evidence where practical.
- Profile-specific emulator configurations.

## M8 — Hardware-aware budgets

- RAM accounting.
- Palette/bitplane/video budgets.
- Blitter-aware STE diagnostics where applicable.
- Frame-budget estimates.
- Audio memory/bandwidth diagnostics.

## M9 — AtariStudio product integration

- RetroStudio Linux editor integration.
- Atari project wizard.
- Target inspector.
- Live hardware budget panels.
- Build/run/export UX.

## M10 — Release candidate

- Complete example games.
- Reproducible Linux packages.
- Documentation/tutorials.
- Real hardware/emulator qualification matrix.
- v0.1.0 release.
