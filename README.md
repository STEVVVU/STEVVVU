<picture><source media="(prefers-color-scheme: dark)" srcset="assets/hero-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/hero-light.svg"><img src="assets/hero-light.svg" alt="Steven Vu. Systems in motion. Storage, compilers, and graphics." width="100%"></picture>

[Explore the work](#selected-work) · [Inside the projects](#inside-the-projects) · [All repositories](https://github.com/STEVVVU?tab=repositories)

I build systems software, developer tools, and graphics. I'm interested in what happens inside: the write that survives a crash, the worker that recovers, and the frame that reaches the screen.

### Selected work

Select a project to inspect the code.

<a href="https://github.com/STEVVVU/stratadb"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/stratadb-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/stratadb-light.svg"><img src="assets/stratadb-light.svg" alt="StrataDB. Checksummed WAL, atomic batches, snapshots, and crash recovery. Open repository." width="400"></picture></a> <a href="https://github.com/STEVVVU/edgeproxy"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/edgeproxy-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/edgeproxy-light.svg"><img src="assets/edgeproxy-light.svg" alt="EdgeProxy. HTTP/1.1 proxy with bounded concurrency, health checks, circuit breakers, and phase-aware retries. Open repository." width="400"></picture></a>

<a href="https://github.com/STEVVVU/durableflow"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/durableflow-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/durableflow-light.svg"><img src="assets/durableflow-light.svg" alt="DurableFlow. Durable job queue with fenced leases, retries, and recovery tests. Open repository." width="400"></picture></a> <a href="https://github.com/STEVVVU/warpforge-mlir"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/warpforge-mlir-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/warpforge-mlir-light.svg"><img src="assets/warpforge-mlir-light.svg" alt="WarpForge. LLVM/MLIR optimization with graph fusion, tiling, vectorization, and progressive lowering. Open repository." width="400"></picture></a>

<a href="https://github.com/STEVVVU/chainindex"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/chainindex-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/chainindex-light.svg"><img src="assets/chainindex-light.svg" alt="ChainIndex. Reorg-aware EVM event indexing with a Solidity escrow contract and deterministic tests. Open repository." width="400"></picture></a> <a href="https://github.com/STEVVVU/lumenforge-webgl"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/lumenforge-webgl-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/lumenforge-webgl-light.svg"><img src="assets/lumenforge-webgl-light.svg" alt="LumenForge. glTF inspection, deferred PBR lighting, object picking, and frame diagnostics. Open repository." width="400"></picture></a>

### Inside the projects

<details>
<summary>Read the architecture and failure models</summary>

- [StrataDB storage architecture](https://github.com/STEVVVU/stratadb/blob/main/docs/architecture.md) and [failure model](https://github.com/STEVVVU/stratadb/blob/main/docs/failure-model.md)
- [EdgeProxy protocol and failure model](https://github.com/STEVVVU/edgeproxy/blob/main/docs/protocol-and-failure-model.md)
- [DurableFlow delivery and recovery guarantees](https://github.com/STEVVVU/durableflow/blob/main/docs/failure-model.md)
- [LumenForge rendering architecture](https://github.com/STEVVVU/lumenforge-webgl/blob/main/docs/ARCHITECTURE.md)

</details>

<details>
<summary>More experiments in languages, compute, and tooling</summary>

- [EmberLang](https://github.com/STEVVVU/emberlang-vm): a Rust compiler and bytecode VM.
- [KernelForge](https://github.com/STEVVVU/kernelforge-gpu): CUDA kernel fusion and correctness checks.
- [Traceframe](https://github.com/STEVVVU/traceframe): a Python execution visualizer.
- [SRE Observatory](https://github.com/STEVVVU/sre-observatory): an infrastructure and observability reference.
- [Microbook](https://github.com/STEVVVU/microbook-quant): market-data ingestion and order-book replay.

</details>

<details>
<summary>See a frame from the LumenForge renderer</summary>

[![LumenForge material-grid scene with deferred lighting, object inspection, and frame diagnostics](https://raw.githubusercontent.com/STEVVVU/lumenforge-webgl/main/artifacts/browser-desktop.png)](https://github.com/STEVVVU/lumenforge-webgl)

</details>

<sub>Original SVG artwork, generated from [source](scripts/render_profile.py). The header settles after 4.6 seconds and respects reduced-motion preferences.</sub>
