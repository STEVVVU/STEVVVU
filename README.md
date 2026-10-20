## Highlights

- Systems software, developer tools, and graphics projects.
- Storage engines, HTTP proxies, durable workers, compilers, WebGL rendering, and EVM event indexing.
- [37 public repositories](https://github.com/STEVVVU?tab=repositories&type=public) as of October 20, 2026.

## Languages and Tools

### Languages

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![C++](https://img.shields.io/badge/C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white) ![Rust](https://img.shields.io/badge/Rust-000000?style=for-the-badge&logo=rust&logoColor=white) ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black) ![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white) ![CUDA](https://img.shields.io/badge/CUDA-76B900?style=for-the-badge&logo=nvidia&logoColor=white)

### Systems, Compilers, and Data

![Tokio](https://img.shields.io/badge/Tokio-000000?style=for-the-badge) ![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white) ![LLVM](https://img.shields.io/badge/LLVM-262D3A?style=for-the-badge&logo=llvm&logoColor=white) ![MLIR](https://img.shields.io/badge/MLIR-4B32C3?style=for-the-badge) ![CMake](https://img.shields.io/badge/CMake-064F8C?style=for-the-badge&logo=cmake&logoColor=white) ![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=prometheus&logoColor=white)

### Web, Testing, and Tools

![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB) ![Node.js](https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white) ![WebGL](https://img.shields.io/badge/WebGL-990000?style=for-the-badge&logo=webgl&logoColor=white) ![glTF](https://img.shields.io/badge/glTF-87C540?style=for-the-badge) ![Vitest](https://img.shields.io/badge/Vitest-6E9F18?style=for-the-badge&logo=vitest&logoColor=white) ![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white) ![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)

<h3>My projects</h3>
<table>
  <thead align="center">
    <tr>
      <td><b>📽️ Projects</b></td>
      <td><b>🛠️ Tools</b></td>
      <td><b>📚 Features</b></td>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="https://github.com/STEVVVU/stratadb"><b>StrataDB</b></a></td>
      <td>
        <img alt="Rust" src="https://img.shields.io/badge/Rust-000000?style=for-the-badge&amp;logo=rust&amp;logoColor=white" />
      </td>
      <td>
        <ul>
          <li>Embedded key-value storage with CRC-32 checksums and atomic write batches.</li>
          <li>Point-in-time snapshots, segment rotation, and copy-forward compaction.</li>
          <li>Active-tail recovery, sealed-segment corruption checks, and fault-injection tests.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><a href="https://github.com/STEVVVU/edgeproxy"><b>EdgeProxy</b></a></td>
      <td>
        <img alt="Rust" src="https://img.shields.io/badge/Rust-000000?style=for-the-badge&amp;logo=rust&amp;logoColor=white" />
        <img alt="Tokio" src="https://img.shields.io/badge/Tokio-000000?style=for-the-badge" />
        <img alt="Prometheus" src="https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&amp;logo=prometheus&amp;logoColor=white" />
      </td>
      <td>
        <ul>
          <li>Async HTTP/1.1 reverse proxy with strict request framing and bounded concurrency.</li>
          <li>Active upstream health checks and per-upstream circuit breakers.</li>
          <li>Phase-aware retries, graceful shutdown, and deterministic integration tests.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><a href="https://github.com/STEVVVU/durableflow"><b>DurableFlow</b></a></td>
      <td>
        <img alt="Python" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&amp;logo=python&amp;logoColor=white" />
        <img alt="SQLite" src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&amp;logo=sqlite&amp;logoColor=white" />
      </td>
      <td>
        <ul>
          <li>Persistent job queue with separate API, coordinator, and worker processes.</li>
          <li>Expiring leases, heartbeats, and stale-worker fencing.</li>
          <li>Retries, cancellation, dead-letter redrive, and a deterministic chaos harness.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><a href="https://github.com/STEVVVU/warpforge-mlir"><b>WarpForge</b></a></td>
      <td>
        <img alt="C++" src="https://img.shields.io/badge/C%2B%2B-00599C?style=for-the-badge&amp;logo=cplusplus&amp;logoColor=white" />
        <img alt="LLVM" src="https://img.shields.io/badge/LLVM-262D3A?style=for-the-badge&amp;logo=llvm&amp;logoColor=white" />
        <img alt="MLIR" src="https://img.shields.io/badge/MLIR-4B32C3?style=for-the-badge" />
      </td>
      <td>
        <ul>
          <li>LLVM/MLIR compiler optimizer for neural-network workloads.</li>
          <li>Matmul epilogue fusion, configurable tiling, and vectorization.</li>
          <li>Shape verification, progressive lowering, and deterministic pass fixtures.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><a href="https://github.com/STEVVVU/lumenforge-webgl"><b>LumenForge</b></a></td>
      <td>
        <img alt="TypeScript" src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&amp;logo=typescript&amp;logoColor=white" />
        <img alt="React" src="https://img.shields.io/badge/React-20232A?style=for-the-badge&amp;logo=react&amp;logoColor=61DAFB" />
        <img alt="WebGL" src="https://img.shields.io/badge/WebGL-990000?style=for-the-badge&amp;logo=webgl&amp;logoColor=white" />
      </td>
      <td>
        <ul>
          <li>WebGL2 renderer and glTF inspector with deferred PBR lighting and shadows.</li>
          <li>GPU object picking, frustum culling, and frame diagnostics.</li>
          <li>Unit tests and browser verification for loading, resize, and context restoration.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><a href="https://github.com/STEVVVU/chainindex"><b>ChainIndex</b></a></td>
      <td>
        <img alt="TypeScript" src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&amp;logo=typescript&amp;logoColor=white" />
        <img alt="SQLite" src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&amp;logo=sqlite&amp;logoColor=white" />
      </td>
      <td>
        <ul>
          <li>EVM event indexing with confirmation-depth processing and transactional checkpoints.</li>
          <li>Resumable backfills and common-ancestor rollback after chain reorganizations.</li>
          <li>Solidity escrow reference contract and deterministic fake-chain tests.</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

<sub>Profile layout follows [osu](https://github.com/osu). Technology badges by [Shields.io](https://shields.io/).</sub>
