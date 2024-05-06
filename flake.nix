{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    flake-utils.url = "github:numtide/flake-utils";
    flake-compat = {
      url = "github:edolstra/flake-compat";
      flake = false;
    };
    rust-overlay.url = "github:oxalica/rust-overlay";
  };
  outputs = {
    self,
    nixpkgs,
    flake-utils,
    rust-overlay,
    ...
  }:
    flake-utils.lib.eachDefaultSystem
    (system: let
      pkgs = import nixpkgs {
        inherit system;
        overlays = [rust-overlay.overlays.default];
      };
      rustVersion = "1.76.0";
      rust = pkgs.rust-bin.stable.${rustVersion}.default.override {
        extensions = [
          "cargo"
          "rust-src" # for rust-analyzer
          "rust-analyzer"
        ];
      };
    in {
      devShells.default = pkgs.mkShell {
        name = "rerun dev shell";
        buildInputs = with pkgs; [
          libxkbcommon
          libGL
          wayland
          pixi
          rust
          # cargo
          # clippy
          # rustfmt
          # rust-analyzer
        ];
        RUST_SRC_PATH = "${pkgs.rustPlatform.rustLibSrc}";
        shellHook = '''';
      };
    })
    // {
      overlays.default = final: prev: {
        # inherit (self.packages.${final.system}) rerun;
      };
    };
}
