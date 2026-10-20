## Work

- **Focus:** Systems software, developer tools, and graphics.
- **Languages:** Rust, Python, TypeScript, C++, JavaScript, and CUDA.
- **Project areas:** Storage engines, HTTP proxies, job orchestration, compiler optimization, WebGL rendering, and event indexing.

## Languages and tools

| Area | Technologies used in my repositories |
| --- | --- |
| Systems and networking | Rust, Tokio, HTTP/1.1 |
| Backend and workers | Python, Node.js, Fastify |
| Frontend and graphics | TypeScript, JavaScript, React, WebGL2, glTF |
| Data and persistence | SQLite, write-ahead logs, transactional checkpoints |
| Compilers and compute | C++, LLVM, MLIR, CUDA, CMake |
| Development and verification | Git, GitHub Actions, unit tests, integration tests, deterministic failure tests |

## Projects

| Repository | Implementation |
| --- | --- |
| [StrataDB](https://github.com/STEVVVU/stratadb) | Rust embedded key-value store. Checksummed WAL, atomic batches, snapshots, crash recovery, and compaction. |
| [EdgeProxy](https://github.com/STEVVVU/edgeproxy) | Async Rust HTTP/1.1 proxy. Bounded concurrency, health checks, circuit breakers, and phase-aware retries. |
| [DurableFlow](https://github.com/STEVVVU/durableflow) | Python job queue with SQLite persistence. Leases, stale-worker fencing, retries, cancellation, and dead-letter redrive. |
| [WarpForge](https://github.com/STEVVVU/warpforge-mlir) | LLVM/MLIR optimizer. Matmul epilogue fusion, tiling, vectorization, and progressive lowering. |
| [LumenForge](https://github.com/STEVVVU/lumenforge-webgl) | TypeScript WebGL2 renderer and glTF inspector. Deferred PBR lighting, shadows, GPU picking, and frame diagnostics. |
| [ChainIndex](https://github.com/STEVVVU/chainindex) | TypeScript EVM event indexer. SQLite checkpoints, resumable backfills, reorganization recovery, and a Solidity escrow contract. |

<details>
<summary>Architecture and failure models</summary>

- [StrataDB storage architecture](https://github.com/STEVVVU/stratadb/blob/main/docs/architecture.md) and [recovery model](https://github.com/STEVVVU/stratadb/blob/main/docs/failure-model.md).
- [EdgeProxy protocol boundaries and retry rules](https://github.com/STEVVVU/edgeproxy/blob/main/docs/protocol-and-failure-model.md).
- [DurableFlow delivery and recovery guarantees](https://github.com/STEVVVU/durableflow/blob/main/docs/failure-model.md).
- [WarpForge compiler pass invariants](https://github.com/STEVVVU/warpforge-mlir/blob/main/docs/PASSES.md).
- [LumenForge rendering architecture](https://github.com/STEVVVU/lumenforge-webgl/blob/main/docs/ARCHITECTURE.md).
- [ChainIndex architecture](https://github.com/STEVVVU/chainindex/blob/main/docs/ARCHITECTURE.md) and [threat model](https://github.com/STEVVVU/chainindex/blob/main/docs/THREAT_MODEL.md).

</details>

## GitHub activity

[37 public repositories](https://github.com/STEVVVU?tab=repositories&type=public) · Snapshot: October 20, 2026.

![Public contribution calendar](./contrib-heatmap.svg)

<sub>Calendar generator: [navi3582/animated-github-profile](https://github.com/navi3582/animated-github-profile), [MIT license](./LICENSE). [Source and regeneration](./scripts/README.md).</sub>
