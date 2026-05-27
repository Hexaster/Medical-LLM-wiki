# Wiki Log

> Chronological record of all wiki actions. Append-only.
> Format: `## [YYYY-MM-DD] action | subject`
> Actions: ingest, update, query, lint, create, archive, delete, merge
> When this file exceeds 500 entries, rotate: rename to `log-YYYY.md` and start fresh.

## [2026-05-26] update | Correct wiki scope
- Corrected repository scope: this is an LLM-generated and LLM-maintained wiki about medicine and healthcare, not a wiki primarily about medical LLMs or clinical AI.
- Updated operating rules in `SCHEMA.md` and `README.md` to prevent irrelevant LLM/AI framing.
- Removed irrelevant LLM/AI relevance sections from `concepts/ems-zones-of-care.md`, `concepts/clinical-workflow-in-high-threat-care.md`, and `concepts/mass-casualty-triage.md`.
- Updated navigation summaries in `index.md`.

## [2026-05-26] ingest | EMS Zones of Care
- Source: https://www.ncbi.nlm.nih.gov/books/NBK436017/
- Raw source saved: `raw/articles/ems-zones-of-care-statpearls-2025.md`
- Created concept pages: `concepts/ems-zones-of-care.md`, `concepts/clinical-workflow-in-high-threat-care.md`, `concepts/mass-casualty-triage.md`
- Updated navigation: `index.md`
- Notes: Source is StatPearls educational content about EMS Hot/Warm/Cold zones of care. It was integrated as medical workflow context for high-threat prehospital care and mass casualty triage.

## [2026-05-26] create | Medical LLM wiki initialized
- Domain: LLM-generated and LLM-maintained wiki about medicine and healthcare.
- Location: `/home/zzz010122/Medical-LLM-wiki`
- Structure created with `SCHEMA.md`, `index.md`, `log.md`, `raw/`, `entities/`, `concepts/`, `comparisons/`, `queries/`, `_meta/`, and `_archive/`.
- Convention: store wiki content and raw ingests in English; translate non-English sources before writing them.

## [2026-05-27] ingest | GeneReviews: 1q21.1 Recurrent Deletion
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK52787/
- Raw extract saved: `raw/articles/genereviews-1q21-1-recurrent-deletion.md`
- Created/updated entity page: `entities/1q21-1-recurrent-deletion.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] create | Core medical concept pages
- Created `concepts/diagnosis.md`, `concepts/pathology.md`, and `concepts/therapeutics.md` to support cross-links from GeneReviews disease summaries.
- Updated navigation: `index.md`.

## [2026-05-27] ingest | GeneReviews: 3-Hydroxyisobutyryl-CoA Hydrolase Deficiency
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK619246/
- Raw extract saved: `raw/articles/genereviews-3-hydroxyisobutyryl-coa-hydrolase-deficiency.md`
- Created/updated entity page: `entities/3-hydroxyisobutyryl-coa-hydrolase-deficiency.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: 3-M Syndrome
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1481/
- Raw extract saved: `raw/articles/genereviews-3-m-syndrome.md`
- Created/updated entity page: `entities/3-m-syndrome.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: 3q29 Recurrent Deletion
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK385289/
- Raw extract saved: `raw/articles/genereviews-3q29-recurrent-deletion.md`
- Created/updated entity page: `entities/3q29-recurrent-deletion.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: 7q11.23 Duplication Syndrome
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK327268/
- Raw extract saved: `raw/articles/genereviews-7q11-23-duplication-syndrome.md`
- Created/updated entity page: `entities/7q11-23-duplication-syndrome.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: 15q13.3 Recurrent Deletion
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK50780/
- Raw extract saved: `raw/articles/genereviews-15q13-3-recurrent-deletion.md`
- Created/updated entity page: `entities/15q13-3-recurrent-deletion.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: 16p11.2 Recurrent Deletion
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK11167/
- Raw extract saved: `raw/articles/genereviews-16p11-2-recurrent-deletion.md`
- Created/updated entity page: `entities/16p11-2-recurrent-deletion.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: 16p12.2 Recurrent Deletion
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK274565/
- Raw extract saved: `raw/articles/genereviews-16p12-2-recurrent-deletion.md`
- Created/updated entity page: `entities/16p12-2-recurrent-deletion.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: 17q12 Recurrent Deletion Syndrome
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK401562/
- Raw extract saved: `raw/articles/genereviews-17q12-recurrent-deletion-syndrome.md`
- Created/updated entity page: `entities/17q12-recurrent-deletion-syndrome.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: 17q12 Recurrent Duplication
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK344340/
- Raw extract saved: `raw/articles/genereviews-17q12-recurrent-duplication.md`
- Created/updated entity page: `entities/17q12-recurrent-duplication.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: 21-Hydroxylase-Deficient Congenital Adrenal Hyperplasia
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1171/
- Raw extract saved: `raw/articles/genereviews-21-hydroxylase-deficient-congenital-adrenal-hyperplasia.md`
- Created/updated entity page: `entities/21-hydroxylase-deficient-congenital-adrenal-hyperplasia.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: 22q11.2 Deletion Syndrome
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1523/
- Raw extract saved: `raw/articles/genereviews-22q11-2-deletion-syndrome.md`
- Created/updated entity page: `entities/22q11-2-deletion-syndrome.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: AARS2 -Related Disorder
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK608563/
- Raw extract saved: `raw/articles/genereviews-aars2-related-disorder.md`
- Created/updated entity page: `entities/aars2-related-disorder.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Abetalipoproteinemia
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK532447/
- Raw extract saved: `raw/articles/genereviews-abetalipoproteinemia.md`
- Created/updated entity page: `entities/abetalipoproteinemia.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Aceruloplasminemia
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1493/
- Raw extract saved: `raw/articles/genereviews-aceruloplasminemia.md`
- Created/updated entity page: `entities/aceruloplasminemia.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Achondrogenesis Type 1B
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1516/
- Raw extract saved: `raw/articles/genereviews-achondrogenesis-type-1b.md`
- Created/updated entity page: `entities/achondrogenesis-type-1b.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Achondroplasia
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1152/
- Raw extract saved: `raw/articles/genereviews-achondroplasia.md`
- Created/updated entity page: `entities/achondroplasia.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Achromatopsia
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1418/
- Raw extract saved: `raw/articles/genereviews-achromatopsia.md`
- Created/updated entity page: `entities/achromatopsia.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Acid Sphingomyelinase Deficiency
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1370/
- Raw extract saved: `raw/articles/genereviews-acid-sphingomyelinase-deficiency.md`
- Created/updated entity page: `entities/acid-sphingomyelinase-deficiency.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: ACTG2 Visceral Myopathy
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK299311/
- Raw extract saved: `raw/articles/genereviews-actg2-visceral-myopathy.md`
- Created/updated entity page: `entities/actg2-visceral-myopathy.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Activated PI3K Delta Syndrome
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK611655/
- Raw extract saved: `raw/articles/genereviews-activated-pi3k-delta-syndrome.md`
- Created/updated entity page: `entities/activated-pi3k-delta-syndrome.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Acute Intermittent Porphyria
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1193/
- Raw extract saved: `raw/articles/genereviews-acute-intermittent-porphyria.md`
- Created/updated entity page: `entities/acute-intermittent-porphyria.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: ADAMTSL4- Related Eye Disorders
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK84111/
- Raw extract saved: `raw/articles/genereviews-adamtsl4-related-eye-disorders.md`
- Created/updated entity page: `entities/adamtsl4-related-eye-disorders.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: ADCY5 -Related Movement Disorder
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK263441/
- Raw extract saved: `raw/articles/genereviews-adcy5-related-movement-disorder.md`
- Created/updated entity page: `entities/adcy5-related-movement-disorder.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Adenine Phosphoribosyltransferase Deficiency
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK100238/
- Raw extract saved: `raw/articles/genereviews-adenine-phosphoribosyltransferase-deficiency.md`
- Created/updated entity page: `entities/adenine-phosphoribosyltransferase-deficiency.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Adenosine Deaminase 2 Deficiency
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK544951/
- Raw extract saved: `raw/articles/genereviews-adenosine-deaminase-2-deficiency.md`
- Created/updated entity page: `entities/adenosine-deaminase-2-deficiency.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Adenosine Deaminase Deficiency
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1483/
- Raw extract saved: `raw/articles/genereviews-adenosine-deaminase-deficiency.md`
- Created/updated entity page: `entities/adenosine-deaminase-deficiency.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: ADNP- Related Helsmoortel-Van der Aa Syndrome
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK355518/
- Raw extract saved: `raw/articles/genereviews-adnp-related-helsmoortel-van-der-aa-syndrome.md`
- Created/updated entity page: `entities/adnp-related-helsmoortel-van-der-aa-syndrome.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Adult Refsum Disease
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1353/
- Raw extract saved: `raw/articles/genereviews-adult-refsum-disease.md`
- Created/updated entity page: `entities/adult-refsum-disease.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: AFF4 -Related CHOPS Syndrome
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK621037/
- Raw extract saved: `raw/articles/genereviews-aff4-related-chops-syndrome.md`
- Created/updated entity page: `entities/aff4-related-chops-syndrome.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: AFG3L2 -Related Neurologic Disorders
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK54582/
- Raw extract saved: `raw/articles/genereviews-afg3l2-related-neurologic-disorders.md`
- Created/updated entity page: `entities/afg3l2-related-neurologic-disorders.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Aicardi-Goutières Syndrome
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1475/
- Raw extract saved: `raw/articles/genereviews-aicardi-gouti-res-syndrome.md`
- Created/updated entity page: `entities/aicardi-gouti-res-syndrome.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Aicardi Syndrome
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1381/
- Raw extract saved: `raw/articles/genereviews-aicardi-syndrome.md`
- Created/updated entity page: `entities/aicardi-syndrome.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: AIP Familial Isolated Pituitary Adenomas
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK97965/
- Raw extract saved: `raw/articles/genereviews-aip-familial-isolated-pituitary-adenomas.md`
- Created/updated entity page: `entities/aip-familial-isolated-pituitary-adenomas.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Alagille Syndrome
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1273/
- Raw extract saved: `raw/articles/genereviews-alagille-syndrome.md`
- Created/updated entity page: `entities/alagille-syndrome.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Alexander Disease
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1172/
- Raw extract saved: `raw/articles/genereviews-alexander-disease.md`
- Created/updated entity page: `entities/alexander-disease.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Alkaptonuria
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1454/
- Raw extract saved: `raw/articles/genereviews-alkaptonuria.md`
- Created/updated entity page: `entities/alkaptonuria.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: ALK -Related Neuroblastic Tumor Susceptibility
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK24599/
- Raw extract saved: `raw/articles/genereviews-alk-related-neuroblastic-tumor-susceptibility.md`
- Created/updated entity page: `entities/alk-related-neuroblastic-tumor-susceptibility.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Allan-Herndon-Dudley Syndrome
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK26373/
- Raw extract saved: `raw/articles/genereviews-allan-herndon-dudley-syndrome.md`
- Created/updated entity page: `entities/allan-herndon-dudley-syndrome.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Alpha-1 Antitrypsin Deficiency
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1519/
- Raw extract saved: `raw/articles/genereviews-alpha-1-antitrypsin-deficiency.md`
- Created/updated entity page: `entities/alpha-1-antitrypsin-deficiency.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Alpha-Mannosidosis
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1396/
- Raw extract saved: `raw/articles/genereviews-alpha-mannosidosis.md`
- Created/updated entity page: `entities/alpha-mannosidosis.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Alpha-Thalassemia
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1435/
- Raw extract saved: `raw/articles/genereviews-alpha-thalassemia.md`
- Created/updated entity page: `entities/alpha-thalassemia.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Alpha-Thalassemia X-Linked Intellectual Disability Syndrome
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1449/
- Raw extract saved: `raw/articles/genereviews-alpha-thalassemia-x-linked-intellectual-disability-syndrome.md`
- Created/updated entity page: `entities/alpha-thalassemia-x-linked-intellectual-disability-syndrome.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: ALPK1- Related Autoinflammatory Disease
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK604494/
- Raw extract saved: `raw/articles/genereviews-alpk1-related-autoinflammatory-disease.md`
- Created/updated entity page: `entities/alpk1-related-autoinflammatory-disease.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Alport Syndrome
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1207/
- Raw extract saved: `raw/articles/genereviews-alport-syndrome.md`
- Created/updated entity page: `entities/alport-syndrome.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: ALS2 -Related Disorder
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1243/
- Raw extract saved: `raw/articles/genereviews-als2-related-disorder.md`
- Created/updated entity page: `entities/als2-related-disorder.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Alström Syndrome
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1267/
- Raw extract saved: `raw/articles/genereviews-alstr-m-syndrome.md`
- Created/updated entity page: `entities/alstr-m-syndrome.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Alzheimer Disease Overview
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1161/
- Raw extract saved: `raw/articles/genereviews-alzheimer-disease-overview.md`
- Created/updated entity page: `entities/alzheimer-disease-overview.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Amyotrophic Lateral Sclerosis Overview
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1450/
- Raw extract saved: `raw/articles/genereviews-amyotrophic-lateral-sclerosis-overview.md`
- Created/updated entity page: `entities/amyotrophic-lateral-sclerosis-overview.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Andersen-Tawil Syndrome
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1264/
- Raw extract saved: `raw/articles/genereviews-andersen-tawil-syndrome.md`
- Created/updated entity page: `entities/andersen-tawil-syndrome.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Androgen Insensitivity Syndrome
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1429/
- Raw extract saved: `raw/articles/genereviews-androgen-insensitivity-syndrome.md`
- Created/updated entity page: `entities/androgen-insensitivity-syndrome.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Angelman Syndrome
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1144/
- Raw extract saved: `raw/articles/genereviews-angelman-syndrome.md`
- Created/updated entity page: `entities/angelman-syndrome.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: ANKRD17 -Related Neurodevelopmental Syndrome
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK588029/
- Raw extract saved: `raw/articles/genereviews-ankrd17-related-neurodevelopmental-syndrome.md`
- Created/updated entity page: `entities/ankrd17-related-neurodevelopmental-syndrome.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: ANKRD26 -Related Thrombocytopenia
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK507664/
- Raw extract saved: `raw/articles/genereviews-ankrd26-related-thrombocytopenia.md`
- Created/updated entity page: `entities/ankrd26-related-thrombocytopenia.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: ANO5 -Related Muscle Disease
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK114459/
- Raw extract saved: `raw/articles/genereviews-ano5-related-muscle-disease.md`
- Created/updated entity page: `entities/ano5-related-muscle-disease.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: AP-4-Associated Hereditary Spastic Paraplegia
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK535153/
- Raw extract saved: `raw/articles/genereviews-ap-4-associated-hereditary-spastic-paraplegia.md`
- Created/updated entity page: `entities/ap-4-associated-hereditary-spastic-paraplegia.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: APC -Associated Polyposis Conditions
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1345/
- Raw extract saved: `raw/articles/genereviews-apc-associated-polyposis-conditions.md`
- Created/updated entity page: `entities/apc-associated-polyposis-conditions.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Apert Syndrome
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK541728/
- Raw extract saved: `raw/articles/genereviews-apert-syndrome.md`
- Created/updated entity page: `entities/apert-syndrome.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: APOB -Related Familial Hypobetalipoproteinemia
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK570370/
- Raw extract saved: `raw/articles/genereviews-apob-related-familial-hypobetalipoproteinemia.md`
- Created/updated entity page: `entities/apob-related-familial-hypobetalipoproteinemia.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Arginase Deficiency
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1159/
- Raw extract saved: `raw/articles/genereviews-arginase-deficiency.md`
- Created/updated entity page: `entities/arginase-deficiency.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Argininosuccinate Lyase Deficiency
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK51784/
- Raw extract saved: `raw/articles/genereviews-argininosuccinate-lyase-deficiency.md`
- Created/updated entity page: `entities/argininosuccinate-lyase-deficiency.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: ARID1B -Related Disorder
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK541502/
- Raw extract saved: `raw/articles/genereviews-arid1b-related-disorder.md`
- Created/updated entity page: `entities/arid1b-related-disorder.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Aromatic L-Amino Acid Decarboxylase Deficiency
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK595821/
- Raw extract saved: `raw/articles/genereviews-aromatic-l-amino-acid-decarboxylase-deficiency.md`
- Created/updated entity page: `entities/aromatic-l-amino-acid-decarboxylase-deficiency.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Arrhythmogenic Right Ventricular Cardiomyopathy Overview
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1131/
- Raw extract saved: `raw/articles/genereviews-arrhythmogenic-right-ventricular-cardiomyopathy-overview.md`
- Created/updated entity page: `entities/arrhythmogenic-right-ventricular-cardiomyopathy-overview.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: ARSACS
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1255/
- Raw extract saved: `raw/articles/genereviews-arsacs.md`
- Created/updated entity page: `entities/arsacs.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Arterial Tortuosity Syndrome
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK253404/
- Raw extract saved: `raw/articles/genereviews-arterial-tortuosity-syndrome.md`
- Created/updated entity page: `entities/arterial-tortuosity-syndrome.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Arylsulfatase A Deficiency
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1130/
- Raw extract saved: `raw/articles/genereviews-arylsulfatase-a-deficiency.md`
- Created/updated entity page: `entities/arylsulfatase-a-deficiency.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: ASAH1 -Related Disorders
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK488189/
- Raw extract saved: `raw/articles/genereviews-asah1-related-disorders.md`
- Created/updated entity page: `entities/asah1-related-disorders.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Asparagine Synthetase Deficiency
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK525916/
- Raw extract saved: `raw/articles/genereviews-asparagine-synthetase-deficiency.md`
- Created/updated entity page: `entities/asparagine-synthetase-deficiency.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Aspartylglucosaminuria
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK599378/
- Raw extract saved: `raw/articles/genereviews-aspartylglucosaminuria.md`
- Created/updated entity page: `entities/aspartylglucosaminuria.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: ASPM Primary Microcephaly
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK555474/
- Raw extract saved: `raw/articles/genereviews-aspm-primary-microcephaly.md`
- Created/updated entity page: `entities/aspm-primary-microcephaly.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: ASXL3 -Related Disorder
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK563693/
- Raw extract saved: `raw/articles/genereviews-asxl3-related-disorder.md`
- Created/updated entity page: `entities/asxl3-related-disorder.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Ataxia-Telangiectasia
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK26468/
- Raw extract saved: `raw/articles/genereviews-ataxia-telangiectasia.md`
- Created/updated entity page: `entities/ataxia-telangiectasia.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Ataxia with Oculomotor Apraxia Type 2
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1154/
- Raw extract saved: `raw/articles/genereviews-ataxia-with-oculomotor-apraxia-type-2.md`
- Created/updated entity page: `entities/ataxia-with-oculomotor-apraxia-type-2.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Ataxia with Vitamin E Deficiency
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1241/
- Raw extract saved: `raw/articles/genereviews-ataxia-with-vitamin-e-deficiency.md`
- Created/updated entity page: `entities/ataxia-with-vitamin-e-deficiency.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: ATN1- Related Neurodevelopmental Disorder
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK583218/
- Raw extract saved: `raw/articles/genereviews-atn1-related-neurodevelopmental-disorder.md`
- Created/updated entity page: `entities/atn1-related-neurodevelopmental-disorder.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: ATP1A3- Related Disorder
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1115/
- Raw extract saved: `raw/articles/genereviews-atp1a3-related-disorder.md`
- Created/updated entity page: `entities/atp1a3-related-disorder.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: ATP6V0A2 -Related Cutis Laxa
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK5200/
- Raw extract saved: `raw/articles/genereviews-atp6v0a2-related-cutis-laxa.md`
- Created/updated entity page: `entities/atp6v0a2-related-cutis-laxa.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: ATP7A -Related Copper Transport Disorders
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1413/
- Raw extract saved: `raw/articles/genereviews-atp7a-related-copper-transport-disorders.md`
- Created/updated entity page: `entities/atp7a-related-copper-transport-disorders.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: ATP8B1 Deficiency
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1297/
- Raw extract saved: `raw/articles/genereviews-atp8b1-deficiency.md`
- Created/updated entity page: `entities/atp8b1-deficiency.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Au-Kline Syndrome
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK540283/
- Raw extract saved: `raw/articles/genereviews-au-kline-syndrome.md`
- Created/updated entity page: `entities/au-kline-syndrome.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Autoimmune Lymphoproliferative Syndrome
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1108/
- Raw extract saved: `raw/articles/genereviews-autoimmune-lymphoproliferative-syndrome.md`
- Created/updated entity page: `entities/autoimmune-lymphoproliferative-syndrome.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Autosomal Dominant Craniometaphyseal Dysplasia
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1461/
- Raw extract saved: `raw/articles/genereviews-autosomal-dominant-craniometaphyseal-dysplasia.md`
- Created/updated entity page: `entities/autosomal-dominant-craniometaphyseal-dysplasia.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Autosomal Dominant Epilepsy with Auditory Features
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1537/
- Raw extract saved: `raw/articles/genereviews-autosomal-dominant-epilepsy-with-auditory-features.md`
- Created/updated entity page: `entities/autosomal-dominant-epilepsy-with-auditory-features.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Autosomal Dominant Robinow Syndrome
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK268648/
- Raw extract saved: `raw/articles/genereviews-autosomal-dominant-robinow-syndrome.md`
- Created/updated entity page: `entities/autosomal-dominant-robinow-syndrome.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Autosomal Dominant Sleep-Related Hypermotor (Hyperkinetic) Epilepsy
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1169/
- Raw extract saved: `raw/articles/genereviews-autosomal-dominant-sleep-related-hypermotor-hyperkinetic-epilepsy.md`
- Created/updated entity page: `entities/autosomal-dominant-sleep-related-hypermotor-hyperkinetic-epilepsy.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Autosomal Dominant TRPV4- Related Disorders
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK201366/
- Raw extract saved: `raw/articles/genereviews-autosomal-dominant-trpv4-related-disorders.md`
- Created/updated entity page: `entities/autosomal-dominant-trpv4-related-disorders.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Autosomal Dominant Tubulointerstitial Kidney Disease – MUC1
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK153723/
- Raw extract saved: `raw/articles/genereviews-autosomal-dominant-tubulointerstitial-kidney-disease-muc1.md`
- Created/updated entity page: `entities/autosomal-dominant-tubulointerstitial-kidney-disease-muc1.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Autosomal Dominant Tubulointerstitial Kidney Disease – REN
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK53700/
- Raw extract saved: `raw/articles/genereviews-autosomal-dominant-tubulointerstitial-kidney-disease-ren.md`
- Created/updated entity page: `entities/autosomal-dominant-tubulointerstitial-kidney-disease-ren.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Autosomal Dominant Tubulointerstitial Kidney Disease – UMOD
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1356/
- Raw extract saved: `raw/articles/genereviews-autosomal-dominant-tubulointerstitial-kidney-disease-umod.md`
- Created/updated entity page: `entities/autosomal-dominant-tubulointerstitial-kidney-disease-umod.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Autosomal Recessive Congenital Ichthyosis
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1420/
- Raw extract saved: `raw/articles/genereviews-autosomal-recessive-congenital-ichthyosis.md`
- Created/updated entity page: `entities/autosomal-recessive-congenital-ichthyosis.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Autosomal Recessive Polycystic Kidney Disease – PKHD1
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1326/
- Raw extract saved: `raw/articles/genereviews-autosomal-recessive-polycystic-kidney-disease-pkhd1.md`
- Created/updated entity page: `entities/autosomal-recessive-polycystic-kidney-disease-pkhd1.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Autosomal Recessive RPE65 -Related Retinal Degeneration
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK549574/
- Raw extract saved: `raw/articles/genereviews-autosomal-recessive-rpe65-related-retinal-degeneration.md`
- Created/updated entity page: `entities/autosomal-recessive-rpe65-related-retinal-degeneration.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Aymé-Gripp Syndrome
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK553534/
- Raw extract saved: `raw/articles/genereviews-aym-gripp-syndrome.md`
- Created/updated entity page: `entities/aym-gripp-syndrome.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Bachmann-Bupp Syndrome
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK583220/
- Raw extract saved: `raw/articles/genereviews-bachmann-bupp-syndrome.md`
- Created/updated entity page: `entities/bachmann-bupp-syndrome.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Baller-Gerold Syndrome
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1204/
- Raw extract saved: `raw/articles/genereviews-baller-gerold-syndrome.md`
- Created/updated entity page: `entities/baller-gerold-syndrome.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: BAP1 Tumor Predisposition Syndrome
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK390611/
- Raw extract saved: `raw/articles/genereviews-bap1-tumor-predisposition-syndrome.md`
- Created/updated entity page: `entities/bap1-tumor-predisposition-syndrome.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Baraitser-Winter Cerebrofrontofacial Syndrome
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK327153/
- Raw extract saved: `raw/articles/genereviews-baraitser-winter-cerebrofrontofacial-syndrome.md`
- Created/updated entity page: `entities/baraitser-winter-cerebrofrontofacial-syndrome.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Bardet-Biedl Syndrome Overview
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1363/
- Raw extract saved: `raw/articles/genereviews-bardet-biedl-syndrome-overview.md`
- Created/updated entity page: `entities/bardet-biedl-syndrome-overview.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Barth Syndrome
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK247162/
- Raw extract saved: `raw/articles/genereviews-barth-syndrome.md`
- Created/updated entity page: `entities/barth-syndrome.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: BCL11A -Related Intellectual Disability
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK547048/
- Raw extract saved: `raw/articles/genereviews-bcl11a-related-intellectual-disability.md`
- Created/updated entity page: `entities/bcl11a-related-intellectual-disability.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Beckwith-Wiedemann Syndrome
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1394/
- Raw extract saved: `raw/articles/genereviews-beckwith-wiedemann-syndrome.md`
- Created/updated entity page: `entities/beckwith-wiedemann-syndrome.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Berardinelli-Seip Congenital Lipodystrophy
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1212/
- Raw extract saved: `raw/articles/genereviews-berardinelli-seip-congenital-lipodystrophy.md`
- Created/updated entity page: `entities/berardinelli-seip-congenital-lipodystrophy.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Bestrophinopathies
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1167/
- Raw extract saved: `raw/articles/genereviews-bestrophinopathies.md`
- Created/updated entity page: `entities/bestrophinopathies.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Beta-Mannosidosis
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK622587/
- Raw extract saved: `raw/articles/genereviews-beta-mannosidosis.md`
- Created/updated entity page: `entities/beta-mannosidosis.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Beta-Propeller Protein-Associated Neurodegeneration
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK424403/
- Raw extract saved: `raw/articles/genereviews-beta-propeller-protein-associated-neurodegeneration.md`
- Created/updated entity page: `entities/beta-propeller-protein-associated-neurodegeneration.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Beta-Thalassemia
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1426/
- Raw extract saved: `raw/articles/genereviews-beta-thalassemia.md`
- Created/updated entity page: `entities/beta-thalassemia.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Bietti Crystalline Dystrophy
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK91457/
- Raw extract saved: `raw/articles/genereviews-bietti-crystalline-dystrophy.md`
- Created/updated entity page: `entities/bietti-crystalline-dystrophy.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Biotinidase Deficiency
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1322/
- Raw extract saved: `raw/articles/genereviews-biotinidase-deficiency.md`
- Created/updated entity page: `entities/biotinidase-deficiency.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Biotin-Thiamine-Responsive Basal Ganglia Disease
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK169615/
- Raw extract saved: `raw/articles/genereviews-biotin-thiamine-responsive-basal-ganglia-disease.md`
- Created/updated entity page: `entities/biotin-thiamine-responsive-basal-ganglia-disease.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Birt-Hogg-Dubé Syndrome
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1522/
- Raw extract saved: `raw/articles/genereviews-birt-hogg-dub-syndrome.md`
- Created/updated entity page: `entities/birt-hogg-dub-syndrome.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Blepharophimosis, Ptosis, and Epicanthus Inversus Syndrome
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1441/
- Raw extract saved: `raw/articles/genereviews-blepharophimosis-ptosis-and-epicanthus-inversus-syndrome.md`
- Created/updated entity page: `entities/blepharophimosis-ptosis-and-epicanthus-inversus-syndrome.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Bloom Syndrome
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1398/
- Raw extract saved: `raw/articles/genereviews-bloom-syndrome.md`
- Created/updated entity page: `entities/bloom-syndrome.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Bohring-Opitz Syndrome
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK481833/
- Raw extract saved: `raw/articles/genereviews-bohring-opitz-syndrome.md`
- Created/updated entity page: `entities/bohring-opitz-syndrome.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Branchiooculofacial Syndrome
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK55063/
- Raw extract saved: `raw/articles/genereviews-branchiooculofacial-syndrome.md`
- Created/updated entity page: `entities/branchiooculofacial-syndrome.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Branchiootorenal Spectrum Disorder
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1380/
- Raw extract saved: `raw/articles/genereviews-branchiootorenal-spectrum-disorder.md`
- Created/updated entity page: `entities/branchiootorenal-spectrum-disorder.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: BRCA1- and BRCA2 -Associated Hereditary Breast and Ovarian Cancer
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1247/
- Raw extract saved: `raw/articles/genereviews-brca1-and-brca2-associated-hereditary-breast-and-ovarian-cancer.md`
- Created/updated entity page: `entities/brca1-and-brca2-associated-hereditary-breast-and-ovarian-cancer.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Brugada Syndrome
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1517/
- Raw extract saved: `raw/articles/genereviews-brugada-syndrome.md`
- Created/updated entity page: `entities/brugada-syndrome.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Bryant-Li-Bhoj Neurodevelopmental Syndrome
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK595206/
- Raw extract saved: `raw/articles/genereviews-bryant-li-bhoj-neurodevelopmental-syndrome.md`
- Created/updated entity page: `entities/bryant-li-bhoj-neurodevelopmental-syndrome.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: BSCL2 -Related Neurologic Disorders / Seipinopathy
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1307/
- Raw extract saved: `raw/articles/genereviews-bscl2-related-neurologic-disorders-seipinopathy.md`
- Created/updated entity page: `entities/bscl2-related-neurologic-disorders-seipinopathy.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: C3 Glomerulopathy
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1425/
- Raw extract saved: `raw/articles/genereviews-c3-glomerulopathy.md`
- Created/updated entity page: `entities/c3-glomerulopathy.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: C9orf72 Frontotemporal Dementia and/or Amyotrophic Lateral Sclerosis
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK268647/
- Raw extract saved: `raw/articles/genereviews-c9orf72-frontotemporal-dementia-and-or-amyotrophic-lateral-sclerosis.md`
- Created/updated entity page: `entities/c9orf72-frontotemporal-dementia-and-or-amyotrophic-lateral-sclerosis.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: CACNA1C -Related Disorders
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1403/
- Raw extract saved: `raw/articles/genereviews-cacna1c-related-disorders.md`
- Created/updated entity page: `entities/cacna1c-related-disorders.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: CADASIL
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1500/
- Raw extract saved: `raw/articles/genereviews-cadasil.md`
- Created/updated entity page: `entities/cadasil.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Caffey Disease
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK99168/
- Raw extract saved: `raw/articles/genereviews-caffey-disease.md`
- Created/updated entity page: `entities/caffey-disease.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Calpainopathy
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1313/
- Raw extract saved: `raw/articles/genereviews-calpainopathy.md`
- Created/updated entity page: `entities/calpainopathy.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Campomelic Dysplasia
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1760/
- Raw extract saved: `raw/articles/genereviews-campomelic-dysplasia.md`
- Created/updated entity page: `entities/campomelic-dysplasia.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Camurati-Engelmann Disease
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1156/
- Raw extract saved: `raw/articles/genereviews-camurati-engelmann-disease.md`
- Created/updated entity page: `entities/camurati-engelmann-disease.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Canavan Disease
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1234/
- Raw extract saved: `raw/articles/genereviews-canavan-disease.md`
- Created/updated entity page: `entities/canavan-disease.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Cantú Syndrome
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK246980/
- Raw extract saved: `raw/articles/genereviews-cant-syndrome.md`
- Created/updated entity page: `entities/cant-syndrome.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Capillary Malformation-Arteriovenous Malformation Syndrome
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK52764/
- Raw extract saved: `raw/articles/genereviews-capillary-malformation-arteriovenous-malformation-syndrome.md`
- Created/updated entity page: `entities/capillary-malformation-arteriovenous-malformation-syndrome.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Carbonic Anhydrase VA Deficiency
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK284774/
- Raw extract saved: `raw/articles/genereviews-carbonic-anhydrase-va-deficiency.md`
- Created/updated entity page: `entities/carbonic-anhydrase-va-deficiency.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Cardiofaciocutaneous Syndrome
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1186/
- Raw extract saved: `raw/articles/genereviews-cardiofaciocutaneous-syndrome.md`
- Created/updated entity page: `entities/cardiofaciocutaneous-syndrome.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Carney Complex
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1286/
- Raw extract saved: `raw/articles/genereviews-carney-complex.md`
- Created/updated entity page: `entities/carney-complex.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Carnitine-Acylcarnitine Translocase Deficiency
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK582032/
- Raw extract saved: `raw/articles/genereviews-carnitine-acylcarnitine-translocase-deficiency.md`
- Created/updated entity page: `entities/carnitine-acylcarnitine-translocase-deficiency.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Carnitine Palmitoyltransferase 1A Deficiency
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1527/
- Raw extract saved: `raw/articles/genereviews-carnitine-palmitoyltransferase-1a-deficiency.md`
- Created/updated entity page: `entities/carnitine-palmitoyltransferase-1a-deficiency.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Carnitine Palmitoyltransferase II Deficiency
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1253/
- Raw extract saved: `raw/articles/genereviews-carnitine-palmitoyltransferase-ii-deficiency.md`
- Created/updated entity page: `entities/carnitine-palmitoyltransferase-ii-deficiency.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Cartilage-Hair Hypoplasia – Anauxetic Dysplasia Spectrum Disorders
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK84550/
- Raw extract saved: `raw/articles/genereviews-cartilage-hair-hypoplasia-anauxetic-dysplasia-spectrum-disorders.md`
- Created/updated entity page: `entities/cartilage-hair-hypoplasia-anauxetic-dysplasia-spectrum-disorders.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: CASK Disorders
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK169825/
- Raw extract saved: `raw/articles/genereviews-cask-disorders.md`
- Created/updated entity page: `entities/cask-disorders.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Catecholaminergic Polymorphic Ventricular Tachycardia
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1289/
- Raw extract saved: `raw/articles/genereviews-catecholaminergic-polymorphic-ventricular-tachycardia.md`
- Created/updated entity page: `entities/catecholaminergic-polymorphic-ventricular-tachycardia.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: CD40 Ligand Deficiency
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1402/
- Raw extract saved: `raw/articles/genereviews-cd40-ligand-deficiency.md`
- Created/updated entity page: `entities/cd40-ligand-deficiency.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: CDC73 -Related Disorders
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK3789/
- Raw extract saved: `raw/articles/genereviews-cdc73-related-disorders.md`
- Created/updated entity page: `entities/cdc73-related-disorders.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: CDK13 -Related Disorder
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK536784/
- Raw extract saved: `raw/articles/genereviews-cdk13-related-disorder.md`
- Created/updated entity page: `entities/cdk13-related-disorder.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: CDKL5 Deficiency Disorder
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK602610/
- Raw extract saved: `raw/articles/genereviews-cdkl5-deficiency-disorder.md`
- Created/updated entity page: `entities/cdkl5-deficiency-disorder.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: CDKN2A Cancer Predisposition
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK616232/
- Raw extract saved: `raw/articles/genereviews-cdkn2a-cancer-predisposition.md`
- Created/updated entity page: `entities/cdkn2a-cancer-predisposition.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: CEBPA- Associated Familial Acute Myeloid Leukemia (AML)
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK47457/
- Raw extract saved: `raw/articles/genereviews-cebpa-associated-familial-acute-myeloid-leukemia-aml.md`
- Created/updated entity page: `entities/cebpa-associated-familial-acute-myeloid-leukemia-aml.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Celiac Disease
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1727/
- Raw extract saved: `raw/articles/genereviews-celiac-disease.md`
- Created/updated entity page: `entities/celiac-disease.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Cerebrotendinous Xanthomatosis
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1409/
- Raw extract saved: `raw/articles/genereviews-cerebrotendinous-xanthomatosis.md`
- Created/updated entity page: `entities/cerebrotendinous-xanthomatosis.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: CETP -Related Hyperalphalipoproteinemia
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK614254/
- Raw extract saved: `raw/articles/genereviews-cetp-related-hyperalphalipoproteinemia.md`
- Created/updated entity page: `entities/cetp-related-hyperalphalipoproteinemia.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Charcot-Marie-Tooth Hereditary Neuropathy Overview
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1358/
- Raw extract saved: `raw/articles/genereviews-charcot-marie-tooth-hereditary-neuropathy-overview.md`
- Created/updated entity page: `entities/charcot-marie-tooth-hereditary-neuropathy-overview.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Char Syndrome
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1106/
- Raw extract saved: `raw/articles/genereviews-char-syndrome.md`
- Created/updated entity page: `entities/char-syndrome.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: CHCHD10 -Related Disorders
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK304142/
- Raw extract saved: `raw/articles/genereviews-chchd10-related-disorders.md`
- Created/updated entity page: `entities/chchd10-related-disorders.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: CHD2 -Related Neurodevelopmental Disorders
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK333201/
- Raw extract saved: `raw/articles/genereviews-chd2-related-neurodevelopmental-disorders.md`
- Created/updated entity page: `entities/chd2-related-neurodevelopmental-disorders.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: CHD4 Neurodevelopmental Disorder
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK561516/
- Raw extract saved: `raw/articles/genereviews-chd4-neurodevelopmental-disorder.md`
- Created/updated entity page: `entities/chd4-neurodevelopmental-disorder.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: CHD7 Disorder
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1117/
- Raw extract saved: `raw/articles/genereviews-chd7-disorder.md`
- Created/updated entity page: `entities/chd7-disorder.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: CHD8 -Related Neurodevelopmental Disorder with Overgrowth
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK585456/
- Raw extract saved: `raw/articles/genereviews-chd8-related-neurodevelopmental-disorder-with-overgrowth.md`
- Created/updated entity page: `entities/chd8-related-neurodevelopmental-disorder-with-overgrowth.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Chediak-Higashi Syndrome
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK5188/
- Raw extract saved: `raw/articles/genereviews-chediak-higashi-syndrome.md`
- Created/updated entity page: `entities/chediak-higashi-syndrome.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: CHEK2 -Related Cancer Predisposition
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK615090/
- Raw extract saved: `raw/articles/genereviews-chek2-related-cancer-predisposition.md`
- Created/updated entity page: `entities/chek2-related-cancer-predisposition.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Cherubism
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1137/
- Raw extract saved: `raw/articles/genereviews-cherubism.md`
- Created/updated entity page: `entities/cherubism.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Childhood Ataxia with Central Nervous System Hypomyelination / Vanishing White Matter
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1258/
- Raw extract saved: `raw/articles/genereviews-childhood-ataxia-with-central-nervous-system-hypomyelination-vanishing-white-matter.md`
- Created/updated entity page: `entities/childhood-ataxia-with-central-nervous-system-hypomyelination-vanishing-white-matter.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: CHKB -Related Muscular Dystrophy
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK589929/
- Raw extract saved: `raw/articles/genereviews-chkb-related-muscular-dystrophy.md`
- Created/updated entity page: `entities/chkb-related-muscular-dystrophy.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: CHMP2B- Related Frontotemporal Dementia-Amyotrophic Lateral Sclerosis
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1199/
- Raw extract saved: `raw/articles/genereviews-chmp2b-related-frontotemporal-dementia-amyotrophic-lateral-sclerosis.md`
- Created/updated entity page: `entities/chmp2b-related-frontotemporal-dementia-amyotrophic-lateral-sclerosis.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Chondrodysplasia Punctata 1, X-Linked
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1544/
- Raw extract saved: `raw/articles/genereviews-chondrodysplasia-punctata-1-x-linked.md`
- Created/updated entity page: `entities/chondrodysplasia-punctata-1-x-linked.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Chondrodysplasia Punctata 2, X-Linked
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK55062/
- Raw extract saved: `raw/articles/genereviews-chondrodysplasia-punctata-2-x-linked.md`
- Created/updated entity page: `entities/chondrodysplasia-punctata-2-x-linked.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Chondrodysplasia with Congenital Joint Dislocations, CHST3 -Related
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK62112/
- Raw extract saved: `raw/articles/genereviews-chondrodysplasia-with-congenital-joint-dislocations-chst3-related.md`
- Created/updated entity page: `entities/chondrodysplasia-with-congenital-joint-dislocations-chst3-related.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Choroideremia
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1337/
- Raw extract saved: `raw/articles/genereviews-choroideremia.md`
- Created/updated entity page: `entities/choroideremia.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Christianson Syndrome
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK475801/
- Raw extract saved: `raw/articles/genereviews-christianson-syndrome.md`
- Created/updated entity page: `entities/christianson-syndrome.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Chronic Granulomatous Disease
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK99496/
- Raw extract saved: `raw/articles/genereviews-chronic-granulomatous-disease.md`
- Created/updated entity page: `entities/chronic-granulomatous-disease.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Chylomicron Retention Disease
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK578949/
- Raw extract saved: `raw/articles/genereviews-chylomicron-retention-disease.md`
- Created/updated entity page: `entities/chylomicron-retention-disease.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Citrin Deficiency
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1181/
- Raw extract saved: `raw/articles/genereviews-citrin-deficiency.md`
- Created/updated entity page: `entities/citrin-deficiency.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Citrullinemia Type I
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1458/
- Raw extract saved: `raw/articles/genereviews-citrullinemia-type-i.md`
- Created/updated entity page: `entities/citrullinemia-type-i.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Classic Ehlers-Danlos Syndrome
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1244/
- Raw extract saved: `raw/articles/genereviews-classic-ehlers-danlos-syndrome.md`
- Created/updated entity page: `entities/classic-ehlers-danlos-syndrome.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Classic Galactosemia and Clinical Variant Galactosemia
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1518/
- Raw extract saved: `raw/articles/genereviews-classic-galactosemia-and-clinical-variant-galactosemia.md`
- Created/updated entity page: `entities/classic-galactosemia-and-clinical-variant-galactosemia.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Classic Isovaleric Acidemia
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK601614/
- Raw extract saved: `raw/articles/genereviews-classic-isovaleric-acidemia.md`
- Created/updated entity page: `entities/classic-isovaleric-acidemia.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Classic Mowat-Wilson Syndrome
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1412/
- Raw extract saved: `raw/articles/genereviews-classic-mowat-wilson-syndrome.md`
- Created/updated entity page: `entities/classic-mowat-wilson-syndrome.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: CLCN2 -Related Leukoencephalopathy
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK326661/
- Raw extract saved: `raw/articles/genereviews-clcn2-related-leukoencephalopathy.md`
- Created/updated entity page: `entities/clcn2-related-leukoencephalopathy.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: CLCN4 -Related Neurodevelopmental Disorder
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK575836/
- Raw extract saved: `raw/articles/genereviews-clcn4-related-neurodevelopmental-disorder.md`
- Created/updated entity page: `entities/clcn4-related-neurodevelopmental-disorder.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: CLCN7 -Related Osteopetrosis
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1127/
- Raw extract saved: `raw/articles/genereviews-clcn7-related-osteopetrosis.md`
- Created/updated entity page: `entities/clcn7-related-osteopetrosis.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Cleidocranial Dysplasia Spectrum Disorder
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1513/
- Raw extract saved: `raw/articles/genereviews-cleidocranial-dysplasia-spectrum-disorder.md`
- Created/updated entity page: `entities/cleidocranial-dysplasia-spectrum-disorder.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: CLPB Deficiency
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK396257/
- Raw extract saved: `raw/articles/genereviews-clpb-deficiency.md`
- Created/updated entity page: `entities/clpb-deficiency.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: CNOT1 -Related Vissers-Bodmer Syndrome
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK621477/
- Raw extract saved: `raw/articles/genereviews-cnot1-related-vissers-bodmer-syndrome.md`
- Created/updated entity page: `entities/cnot1-related-vissers-bodmer-syndrome.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Cockayne Syndrome
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1342/
- Raw extract saved: `raw/articles/genereviews-cockayne-syndrome.md`
- Created/updated entity page: `entities/cockayne-syndrome.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Coffin-Siris Syndrome
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK131811/
- Raw extract saved: `raw/articles/genereviews-coffin-siris-syndrome.md`
- Created/updated entity page: `entities/coffin-siris-syndrome.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Cohen Syndrome
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1482/
- Raw extract saved: `raw/articles/genereviews-cohen-syndrome.md`
- Created/updated entity page: `entities/cohen-syndrome.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: COL1A1 - and COL1A2 -Related Osteogenesis Imperfecta
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1295/
- Raw extract saved: `raw/articles/genereviews-col1a1-and-col1a2-related-osteogenesis-imperfecta.md`
- Created/updated entity page: `entities/col1a1-and-col1a2-related-osteogenesis-imperfecta.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: COL4A1 -Related Disorders
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK7046/
- Raw extract saved: `raw/articles/genereviews-col4a1-related-disorders.md`
- Created/updated entity page: `entities/col4a1-related-disorders.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Cold-Induced Sweating Syndrome Including Crisponi Syndrome
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK52917/
- Raw extract saved: `raw/articles/genereviews-cold-induced-sweating-syndrome-including-crisponi-syndrome.md`
- Created/updated entity page: `entities/cold-induced-sweating-syndrome-including-crisponi-syndrome.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Collagen VI-Related Dystrophies
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1503/
- Raw extract saved: `raw/articles/genereviews-collagen-vi-related-dystrophies.md`
- Created/updated entity page: `entities/collagen-vi-related-dystrophies.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Complete Plasminogen Activator Inhibitor 1 Deficiency
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK447152/
- Raw extract saved: `raw/articles/genereviews-complete-plasminogen-activator-inhibitor-1-deficiency.md`
- Created/updated entity page: `entities/complete-plasminogen-activator-inhibitor-1-deficiency.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: COMP -Related Pseudoachondroplasia
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1487/
- Raw extract saved: `raw/articles/genereviews-comp-related-pseudoachondroplasia.md`
- Created/updated entity page: `entities/comp-related-pseudoachondroplasia.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Congenital Central Hypoventilation Syndrome
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1427/
- Raw extract saved: `raw/articles/genereviews-congenital-central-hypoventilation-syndrome.md`
- Created/updated entity page: `entities/congenital-central-hypoventilation-syndrome.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Congenital Contractural Arachnodactyly
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1386/
- Raw extract saved: `raw/articles/genereviews-congenital-contractural-arachnodactyly.md`
- Created/updated entity page: `entities/congenital-contractural-arachnodactyly.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Congenital Deafness with Labyrinthine Aplasia, Microtia, and Microdontia
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK100664/
- Raw extract saved: `raw/articles/genereviews-congenital-deafness-with-labyrinthine-aplasia-microtia-and-microdontia.md`
- Created/updated entity page: `entities/congenital-deafness-with-labyrinthine-aplasia-microtia-and-microdontia.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Congenital Disorders of N-Linked Glycosylation and Multiple Pathway Overview
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1332/
- Raw extract saved: `raw/articles/genereviews-congenital-disorders-of-n-linked-glycosylation-and-multiple-pathway-overview.md`
- Created/updated entity page: `entities/congenital-disorders-of-n-linked-glycosylation-and-multiple-pathway-overview.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Congenital Dyserythropoietic Anemia Type I
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK5313/
- Raw extract saved: `raw/articles/genereviews-congenital-dyserythropoietic-anemia-type-i.md`
- Created/updated entity page: `entities/congenital-dyserythropoietic-anemia-type-i.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Congenital Erythropoietic Porphyria
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK154652/
- Raw extract saved: `raw/articles/genereviews-congenital-erythropoietic-porphyria.md`
- Created/updated entity page: `entities/congenital-erythropoietic-porphyria.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Congenital Fibrosis of the Extraocular Muscles Overview
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1348/
- Raw extract saved: `raw/articles/genereviews-congenital-fibrosis-of-the-extraocular-muscles-overview.md`
- Created/updated entity page: `entities/congenital-fibrosis-of-the-extraocular-muscles-overview.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Congenital Insensitivity to Pain Overview
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK481553/
- Raw extract saved: `raw/articles/genereviews-congenital-insensitivity-to-pain-overview.md`
- Created/updated entity page: `entities/congenital-insensitivity-to-pain-overview.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Congenital Mirror Movements
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK279760/
- Raw extract saved: `raw/articles/genereviews-congenital-mirror-movements.md`
- Created/updated entity page: `entities/congenital-mirror-movements.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Congenital Myasthenic Syndromes Overview
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1168/
- Raw extract saved: `raw/articles/genereviews-congenital-myasthenic-syndromes-overview.md`
- Created/updated entity page: `entities/congenital-myasthenic-syndromes-overview.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Congenital NAD Deficiency Disorder
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK593504/
- Raw extract saved: `raw/articles/genereviews-congenital-nad-deficiency-disorder.md`
- Created/updated entity page: `entities/congenital-nad-deficiency-disorder.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Congenital Stromal Corneal Dystrophy
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK2690/
- Raw extract saved: `raw/articles/genereviews-congenital-stromal-corneal-dystrophy.md`
- Created/updated entity page: `entities/congenital-stromal-corneal-dystrophy.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Cornelia de Lange Syndrome
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1104/
- Raw extract saved: `raw/articles/genereviews-cornelia-de-lange-syndrome.md`
- Created/updated entity page: `entities/cornelia-de-lange-syndrome.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Costeff Syndrome
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1473/
- Raw extract saved: `raw/articles/genereviews-costeff-syndrome.md`
- Created/updated entity page: `entities/costeff-syndrome.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Cranioectodermal Dysplasia
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK154653/
- Raw extract saved: `raw/articles/genereviews-cranioectodermal-dysplasia.md`
- Created/updated entity page: `entities/cranioectodermal-dysplasia.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Creatine Deficiency Disorders
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK3794/
- Raw extract saved: `raw/articles/genereviews-creatine-deficiency-disorders.md`
- Created/updated entity page: `entities/creatine-deficiency-disorders.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: CSF1R -Related Disorder
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK100239/
- Raw extract saved: `raw/articles/genereviews-csf1r-related-disorder.md`
- Created/updated entity page: `entities/csf1r-related-disorder.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: CSNK2B -Related Neurodevelopmental Disorder
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK606532/
- Raw extract saved: `raw/articles/genereviews-csnk2b-related-neurodevelopmental-disorder.md`
- Created/updated entity page: `entities/csnk2b-related-neurodevelopmental-disorder.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: CTCF -Related Disorder
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK603087/
- Raw extract saved: `raw/articles/genereviews-ctcf-related-disorder.md`
- Created/updated entity page: `entities/ctcf-related-disorder.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: CTDP1 -Related Congenital Cataracts, Facial Dysmorphism, and Neuropathy
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK25565/
- Raw extract saved: `raw/articles/genereviews-ctdp1-related-congenital-cataracts-facial-dysmorphism-and-neuropathy.md`
- Created/updated entity page: `entities/ctdp1-related-congenital-cataracts-facial-dysmorphism-and-neuropathy.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: CTNNB1 Neurodevelopmental Disorder
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK580527/
- Raw extract saved: `raw/articles/genereviews-ctnnb1-neurodevelopmental-disorder.md`
- Created/updated entity page: `entities/ctnnb1-neurodevelopmental-disorder.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: CYLD Cutaneous Syndrome
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK555820/
- Raw extract saved: `raw/articles/genereviews-cyld-cutaneous-syndrome.md`
- Created/updated entity page: `entities/cyld-cutaneous-syndrome.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Cystic Fibrosis
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1250/
- Raw extract saved: `raw/articles/genereviews-cystic-fibrosis.md`
- Created/updated entity page: `entities/cystic-fibrosis.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Cystinosis
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1400/
- Raw extract saved: `raw/articles/genereviews-cystinosis.md`
- Created/updated entity page: `entities/cystinosis.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Cystinuria
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK619248/
- Raw extract saved: `raw/articles/genereviews-cystinuria.md`
- Created/updated entity page: `entities/cystinuria.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Cytochrome P450 Oxidoreductase Deficiency
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1419/
- Raw extract saved: `raw/articles/genereviews-cytochrome-p450-oxidoreductase-deficiency.md`
- Created/updated entity page: `entities/cytochrome-p450-oxidoreductase-deficiency.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Danon Disease
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK554742/
- Raw extract saved: `raw/articles/genereviews-danon-disease.md`
- Created/updated entity page: `entities/danon-disease.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: DBA Syndrome
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK7047/
- Raw extract saved: `raw/articles/genereviews-dba-syndrome.md`
- Created/updated entity page: `entities/dba-syndrome.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: DCTN1 -Related Neurodegeneration
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK47027/
- Raw extract saved: `raw/articles/genereviews-dctn1-related-neurodegeneration.md`
- Created/updated entity page: `entities/dctn1-related-neurodegeneration.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: DCX -Related Disorders
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1185/
- Raw extract saved: `raw/articles/genereviews-dcx-related-disorders.md`
- Created/updated entity page: `entities/dcx-related-disorders.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: DDX11 -Related Cohesinopathy
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK541972/
- Raw extract saved: `raw/articles/genereviews-ddx11-related-cohesinopathy.md`
- Created/updated entity page: `entities/ddx11-related-cohesinopathy.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: DDX3X -Related Neurodevelopmental Disorder
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK561282/
- Raw extract saved: `raw/articles/genereviews-ddx3x-related-neurodevelopmental-disorder.md`
- Created/updated entity page: `entities/ddx3x-related-neurodevelopmental-disorder.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: DDX41 -Associated Familial Myelodysplastic Syndrome and Acute Myeloid Leukemia
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK574843/
- Raw extract saved: `raw/articles/genereviews-ddx41-associated-familial-myelodysplastic-syndrome-and-acute-myeloid-leukemia.md`
- Created/updated entity page: `entities/ddx41-associated-familial-myelodysplastic-syndrome-and-acute-myeloid-leukemia.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Deafness-Dystonia-Optic Neuronopathy Syndrome
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1216/
- Raw extract saved: `raw/articles/genereviews-deafness-dystonia-optic-neuronopathy-syndrome.md`
- Created/updated entity page: `entities/deafness-dystonia-optic-neuronopathy-syndrome.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Dent Disease
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK99494/
- Raw extract saved: `raw/articles/genereviews-dent-disease.md`
- Created/updated entity page: `entities/dent-disease.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Deoxyguanosine Kinase Deficiency
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK7040/
- Raw extract saved: `raw/articles/genereviews-deoxyguanosine-kinase-deficiency.md`
- Created/updated entity page: `entities/deoxyguanosine-kinase-deficiency.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: DEPDC5 -Related Epilepsy
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK385626/
- Raw extract saved: `raw/articles/genereviews-depdc5-related-epilepsy.md`
- Created/updated entity page: `entities/depdc5-related-epilepsy.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: DFNA2 Nonsyndromic Hearing Loss
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1209/
- Raw extract saved: `raw/articles/genereviews-dfna2-nonsyndromic-hearing-loss.md`
- Created/updated entity page: `entities/dfna2-nonsyndromic-hearing-loss.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Diabetes Mellitus, 6q24-Related Transient Neonatal
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1534/
- Raw extract saved: `raw/articles/genereviews-diabetes-mellitus-6q24-related-transient-neonatal.md`
- Created/updated entity page: `entities/diabetes-mellitus-6q24-related-transient-neonatal.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Diastrophic Dysplasia
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1350/
- Raw extract saved: `raw/articles/genereviews-diastrophic-dysplasia.md`
- Created/updated entity page: `entities/diastrophic-dysplasia.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: DICER1- Related Tumor Predisposition
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK196157/
- Raw extract saved: `raw/articles/genereviews-dicer1-related-tumor-predisposition.md`
- Created/updated entity page: `entities/dicer1-related-tumor-predisposition.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Diffuse Gastric and Lobular Breast Cancer Syndrome
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1139/
- Raw extract saved: `raw/articles/genereviews-diffuse-gastric-and-lobular-breast-cancer-syndrome.md`
- Created/updated entity page: `entities/diffuse-gastric-and-lobular-breast-cancer-syndrome.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Dihydrolipoamide Dehydrogenase Deficiency
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK220444/
- Raw extract saved: `raw/articles/genereviews-dihydrolipoamide-dehydrogenase-deficiency.md`
- Created/updated entity page: `entities/dihydrolipoamide-dehydrogenase-deficiency.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Dilated Cardiomyopathy Overview
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1309/
- Raw extract saved: `raw/articles/genereviews-dilated-cardiomyopathy-overview.md`
- Created/updated entity page: `entities/dilated-cardiomyopathy-overview.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Disorders of GNAS Inactivation
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK459117/
- Raw extract saved: `raw/articles/genereviews-disorders-of-gnas-inactivation.md`
- Created/updated entity page: `entities/disorders-of-gnas-inactivation.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Disorders of Intracellular Cobalamin Metabolism
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1328/
- Raw extract saved: `raw/articles/genereviews-disorders-of-intracellular-cobalamin-metabolism.md`
- Created/updated entity page: `entities/disorders-of-intracellular-cobalamin-metabolism.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: DLG4 -Related Synaptopathy
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK592682/
- Raw extract saved: `raw/articles/genereviews-dlg4-related-synaptopathy.md`
- Created/updated entity page: `entities/dlg4-related-synaptopathy.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: DNAJC6 Parkinson Disease
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK570369/
- Raw extract saved: `raw/articles/genereviews-dnajc6-parkinson-disease.md`
- Created/updated entity page: `entities/dnajc6-parkinson-disease.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: DNMT1 -Related Disorder
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK84112/
- Raw extract saved: `raw/articles/genereviews-dnmt1-related-disorder.md`
- Created/updated entity page: `entities/dnmt1-related-disorder.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Donnai-Barrow Syndrome
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1878/
- Raw extract saved: `raw/articles/genereviews-donnai-barrow-syndrome.md`
- Created/updated entity page: `entities/donnai-barrow-syndrome.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Dopamine Beta-Hydroxylase Deficiency
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1474/
- Raw extract saved: `raw/articles/genereviews-dopamine-beta-hydroxylase-deficiency.md`
- Created/updated entity page: `entities/dopamine-beta-hydroxylase-deficiency.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: DRPLA
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1491/
- Raw extract saved: `raw/articles/genereviews-drpla.md`
- Created/updated entity page: `entities/drpla.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Duane Syndrome
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1190/
- Raw extract saved: `raw/articles/genereviews-duane-syndrome.md`
- Created/updated entity page: `entities/duane-syndrome.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Duarte Galactosemia
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK258640/
- Raw extract saved: `raw/articles/genereviews-duarte-galactosemia.md`
- Created/updated entity page: `entities/duarte-galactosemia.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: DYNC1H1 -Related Disorders
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK601997/
- Raw extract saved: `raw/articles/genereviews-dync1h1-related-disorders.md`
- Created/updated entity page: `entities/dync1h1-related-disorders.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: DYRK1A Syndrome
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK333438/
- Raw extract saved: `raw/articles/genereviews-dyrk1a-syndrome.md`
- Created/updated entity page: `entities/dyrk1a-syndrome.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Dysferlinopathy
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1303/
- Raw extract saved: `raw/articles/genereviews-dysferlinopathy.md`
- Created/updated entity page: `entities/dysferlinopathy.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Dyskeratosis Congenita and Related Telomere Biology Disorders
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK22301/
- Raw extract saved: `raw/articles/genereviews-dyskeratosis-congenita-and-related-telomere-biology-disorders.md`
- Created/updated entity page: `entities/dyskeratosis-congenita-and-related-telomere-biology-disorders.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Dystrophic Epidermolysis Bullosa
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1304/
- Raw extract saved: `raw/articles/genereviews-dystrophic-epidermolysis-bullosa.md`
- Created/updated entity page: `entities/dystrophic-epidermolysis-bullosa.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Dystrophinopathies
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1119/
- Raw extract saved: `raw/articles/genereviews-dystrophinopathies.md`
- Created/updated entity page: `entities/dystrophinopathies.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: DYT- GNAL
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK535640/
- Raw extract saved: `raw/articles/genereviews-dyt-gnal.md`
- Created/updated entity page: `entities/dyt-gnal.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: DYT- TOR1A
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1492/
- Raw extract saved: `raw/articles/genereviews-dyt-tor1a.md`
- Created/updated entity page: `entities/dyt-tor1a.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: EBF3 Neurodevelopmental Disorder
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK570204/
- Raw extract saved: `raw/articles/genereviews-ebf3-neurodevelopmental-disorder.md`
- Created/updated entity page: `entities/ebf3-neurodevelopmental-disorder.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: EED -Related Overgrowth
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK540017/
- Raw extract saved: `raw/articles/genereviews-eed-related-overgrowth.md`
- Created/updated entity page: `entities/eed-related-overgrowth.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: EFEMP2 -Related Cutis Laxa
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK54467/
- Raw extract saved: `raw/articles/genereviews-efemp2-related-cutis-laxa.md`
- Created/updated entity page: `entities/efemp2-related-cutis-laxa.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: ELANE -Related Neutropenia
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1533/
- Raw extract saved: `raw/articles/genereviews-elane-related-neutropenia.md`
- Created/updated entity page: `entities/elane-related-neutropenia.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: El-Hattab-Alkuraya Syndrome
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK584547/
- Raw extract saved: `raw/articles/genereviews-el-hattab-alkuraya-syndrome.md`
- Created/updated entity page: `entities/el-hattab-alkuraya-syndrome.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Ellis-van Creveld Syndrome
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK596643/
- Raw extract saved: `raw/articles/genereviews-ellis-van-creveld-syndrome.md`
- Created/updated entity page: `entities/ellis-van-creveld-syndrome.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: ELN -Related Cutis Laxa
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK584550/
- Raw extract saved: `raw/articles/genereviews-eln-related-cutis-laxa.md`
- Created/updated entity page: `entities/eln-related-cutis-laxa.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Emanuel Syndrome
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1263/
- Raw extract saved: `raw/articles/genereviews-emanuel-syndrome.md`
- Created/updated entity page: `entities/emanuel-syndrome.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: EMC10 -Related Neurodevelopmental Disorder
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK592645/
- Raw extract saved: `raw/articles/genereviews-emc10-related-neurodevelopmental-disorder.md`
- Created/updated entity page: `entities/emc10-related-neurodevelopmental-disorder.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Emery-Dreifuss Muscular Dystrophy
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1436/
- Raw extract saved: `raw/articles/genereviews-emery-dreifuss-muscular-dystrophy.md`
- Created/updated entity page: `entities/emery-dreifuss-muscular-dystrophy.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Encephalocraniocutaneous Lipomatosis
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK576966/
- Raw extract saved: `raw/articles/genereviews-encephalocraniocutaneous-lipomatosis.md`
- Created/updated entity page: `entities/encephalocraniocutaneous-lipomatosis.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Enlarged Parietal Foramina
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1128/
- Raw extract saved: `raw/articles/genereviews-enlarged-parietal-foramina.md`
- Created/updated entity page: `entities/enlarged-parietal-foramina.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: ENTPD1 -Related Neurodevelopmental Disorder
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK592266/
- Raw extract saved: `raw/articles/genereviews-entpd1-related-neurodevelopmental-disorder.md`
- Created/updated entity page: `entities/entpd1-related-neurodevelopmental-disorder.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: EPB42 -Related Hereditary Spherocytosis
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK190102/
- Raw extract saved: `raw/articles/genereviews-epb42-related-hereditary-spherocytosis.md`
- Created/updated entity page: `entities/epb42-related-hereditary-spherocytosis.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: EPG5 -Related Disorder
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK584989/
- Raw extract saved: `raw/articles/genereviews-epg5-related-disorder.md`
- Created/updated entity page: `entities/epg5-related-disorder.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Epidermolysis Bullosa Simplex
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1369/
- Raw extract saved: `raw/articles/genereviews-epidermolysis-bullosa-simplex.md`
- Created/updated entity page: `entities/epidermolysis-bullosa-simplex.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Epidermolysis Bullosa with Pyloric Atresia
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1157/
- Raw extract saved: `raw/articles/genereviews-epidermolysis-bullosa-with-pyloric-atresia.md`
- Created/updated entity page: `entities/epidermolysis-bullosa-with-pyloric-atresia.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Epimerase Deficiency Galactosemia
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK51671/
- Raw extract saved: `raw/articles/genereviews-epimerase-deficiency-galactosemia.md`
- Created/updated entity page: `entities/epimerase-deficiency-galactosemia.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Episodic Ataxia Type 1
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK25442/
- Raw extract saved: `raw/articles/genereviews-episodic-ataxia-type-1.md`
- Created/updated entity page: `entities/episodic-ataxia-type-1.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Erythropoietic Protoporphyria, Autosomal Recessive
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK100826/
- Raw extract saved: `raw/articles/genereviews-erythropoietic-protoporphyria-autosomal-recessive.md`
- Created/updated entity page: `entities/erythropoietic-protoporphyria-autosomal-recessive.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: ESCO2 Spectrum Disorder
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1153/
- Raw extract saved: `raw/articles/genereviews-esco2-spectrum-disorder.md`
- Created/updated entity page: `entities/esco2-spectrum-disorder.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Ethylmalonic Encephalopathy
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK453432/
- Raw extract saved: `raw/articles/genereviews-ethylmalonic-encephalopathy.md`
- Created/updated entity page: `entities/ethylmalonic-encephalopathy.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: ETV6- Related Thrombocytopenia and Predisposition to Leukemia
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK564234/
- Raw extract saved: `raw/articles/genereviews-etv6-related-thrombocytopenia-and-predisposition-to-leukemia.md`
- Created/updated entity page: `entities/etv6-related-thrombocytopenia-and-predisposition-to-leukemia.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: EXOC6B -Related Spondyloepimetaphyseal Dysplasia with Joint Laxity
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK592183/
- Raw extract saved: `raw/articles/genereviews-exoc6b-related-spondyloepimetaphyseal-dysplasia-with-joint-laxity.md`
- Created/updated entity page: `entities/exoc6b-related-spondyloepimetaphyseal-dysplasia-with-joint-laxity.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: EXOSC3 Pontocerebellar Hypoplasia
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK236968/
- Raw extract saved: `raw/articles/genereviews-exosc3-pontocerebellar-hypoplasia.md`
- Created/updated entity page: `entities/exosc3-pontocerebellar-hypoplasia.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: EZH2 -Related Overgrowth
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK148820/
- Raw extract saved: `raw/articles/genereviews-ezh2-related-overgrowth.md`
- Created/updated entity page: `entities/ezh2-related-overgrowth.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Fabry Disease
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1292/
- Raw extract saved: `raw/articles/genereviews-fabry-disease.md`
- Created/updated entity page: `entities/fabry-disease.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Facioscapulohumeral Muscular Dystrophy
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1443/
- Raw extract saved: `raw/articles/genereviews-facioscapulohumeral-muscular-dystrophy.md`
- Created/updated entity page: `entities/facioscapulohumeral-muscular-dystrophy.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Factor V Leiden Thrombophilia
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1368/
- Raw extract saved: `raw/articles/genereviews-factor-v-leiden-thrombophilia.md`
- Created/updated entity page: `entities/factor-v-leiden-thrombophilia.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: FAM111A -Related Skeletal Dysplasias
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK590151/
- Raw extract saved: `raw/articles/genereviews-fam111a-related-skeletal-dysplasias.md`
- Created/updated entity page: `entities/fam111a-related-skeletal-dysplasias.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Familial Cerebral Cavernous Malformations
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1293/
- Raw extract saved: `raw/articles/genereviews-familial-cerebral-cavernous-malformations.md`
- Created/updated entity page: `entities/familial-cerebral-cavernous-malformations.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Familial Combined Hypolipidemia
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK593236/
- Raw extract saved: `raw/articles/genereviews-familial-combined-hypolipidemia.md`
- Created/updated entity page: `entities/familial-combined-hypolipidemia.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Familial Dysautonomia
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1180/
- Raw extract saved: `raw/articles/genereviews-familial-dysautonomia.md`
- Created/updated entity page: `entities/familial-dysautonomia.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Familial Hemiplegic Migraine
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1388/
- Raw extract saved: `raw/articles/genereviews-familial-hemiplegic-migraine.md`
- Created/updated entity page: `entities/familial-hemiplegic-migraine.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Familial Hemophagocytic Lymphohistiocytosis
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1444/
- Raw extract saved: `raw/articles/genereviews-familial-hemophagocytic-lymphohistiocytosis.md`
- Created/updated entity page: `entities/familial-hemophagocytic-lymphohistiocytosis.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Familial Hypercholesterolemia
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK174884/
- Raw extract saved: `raw/articles/genereviews-familial-hypercholesterolemia.md`
- Created/updated entity page: `entities/familial-hypercholesterolemia.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Familial Lipoprotein Lipase Deficiency
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1308/
- Raw extract saved: `raw/articles/genereviews-familial-lipoprotein-lipase-deficiency.md`
- Created/updated entity page: `entities/familial-lipoprotein-lipase-deficiency.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Familial Mediterranean Fever
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1227/
- Raw extract saved: `raw/articles/genereviews-familial-mediterranean-fever.md`
- Created/updated entity page: `entities/familial-mediterranean-fever.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Familial Paroxysmal Nonkinesigenic Dyskinesia
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK1221/
- Raw extract saved: `raw/articles/genereviews-familial-paroxysmal-nonkinesigenic-dyskinesia.md`
- Created/updated entity page: `entities/familial-paroxysmal-nonkinesigenic-dyskinesia.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.

## [2026-05-27] ingest | GeneReviews: Familial Porphyria Cutanea Tarda
- Source: GeneReviews/NCBI Bookshelf chapter, https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Chapter URL: https://www.ncbi.nlm.nih.gov/books/NBK143129/
- Raw extract saved: `raw/articles/genereviews-familial-porphyria-cutanea-tarda.md`
- Created/updated entity page: `entities/familial-porphyria-cutanea-tarda.md`
- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.
