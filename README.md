# Malaria Gene Annotation Workflow

This is an assignment for the Exercise: Workflows and FAIR principles in BERN02.

**Goal:** Merge BLASTX protein descriptions into FASTA headers for malaria gene sequences and produce a curated FASTA-like output.

**Keywords:** malaria, bioinformatics, BLASTX, FASTA, reproducibility, FAIR, workflow


## Assumptions
- FASTA header fields are **tab-delimited**, with the first token being the gene ID (e.g., `1_g`).
- BLASTX table is **tab-delimited**; column 1 is gene ID and column 10 is protein description.
- Entries with `null` in the description are **excluded** from the output.

---

## Dependency versions

**Python 3.12** — stable baseline.

**matplotlib 3.9.2, biopython 1.83, nbformat 5.10.4*** — fixed to keep plotting, bioinformatics functions, and notebooks consistent.

---

## Notes on quality control
- Headers remain tab-delimited.
- Sequences are assumed to be single-line (per the original assignment). If multi-line FASTA is needed, see the notebook section “Notes on robustness”.
