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
