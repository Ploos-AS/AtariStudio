# AtariStudio

AtariStudio is the Atari-focused frontend/backend for the RetroStudio game-development platform.

It provides Atari target profiles, hardware-aware validation, asset conversion, runtime/build integration and emulator launch support while keeping generic editor and project logic in **RetroStudio**.

## M0 goals

- Define AtariStudio's boundary relative to RetroStudio.
- Establish initial Atari target profiles.
- Add a minimal RetroStudio target descriptor.
- Add host-side checks and GitHub Actions CI.
- Document the roadmap toward a complete Linux-to-Atari game-development workflow.

## Initial targets

- Atari ST / 68000
- Atari STE / 68000
- Atari TT / 68030
- Atari Falcon / 68030

The ST/STE path is the compatibility baseline. TT and Falcon are explicit target families rather than assumptions baked into the shared core.

## Architecture

```text
AtariStudio
  |
  +-- Atari target profiles
  +-- graphics/audio conversion
  +-- hardware budgets/diagnostics
  +-- Atari runtime/build backend
  +-- packaging and emulator integration
  |
  +--> RetroStudio Core
```

Generic scenes, entities, assets, scripting interfaces, build graphs and Linux editor infrastructure belong in RetroStudio.

See `docs/ARCHITECTURE.md`.

## M0 check

```sh
make check
```

No Atari compiler, ROM/TOS image or emulator is required for M0.

## Status

**M0 — Foundation:** implemented.

## License

MIT. See `LICENSE`.
