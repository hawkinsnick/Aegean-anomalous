# Attribution review

All five controls; 14/15/16 segmentation histories and classification arguments remain source-specific. Boundary bars cannot automatically explain the Malia count difference.

Existing source consultation receipts and limits are inherited exactly from the referenced native packets. This pass inspects those packets, not the underlying publications afresh. No exhaustive literature search, new autopsy or independent review is claimed.

The complete selections below name the finite native collections reviewed. Other repository records and the broader literature are outside this checkpoint. Case counts are review tasks, not inscriptions, independent witnesses or fully attributed alternative pairs.

| Complete native selection | Rows |
|---|---:|
| `research/disagreement-register.json/items` | 5 |

Use the case query to read the finding together with the complete native evidence, including any named author/publication, source locator, inspection state, qualification and source dependence. Missing metadata stays missing; a source ID alone is not proof of direct consultation.

```sh
python scripts/attribution_review.py --check
python scripts/attribution_review.py --case 'ANO-DIS-001'
python scripts/evidence_query.py --list attribution-review
```

| Review ID | Type | Finding | Remaining work |
|---|---|---|---|
| ANO-DIS-001 | CLASSIFICATION | Museum metadata, Flouda classification and later review scope are different kinds of source assertion, not independent votes for a script. | Locate source-specific classification arguments and retain disputed writing/script status. |
| ANO-DIS-002 | INTERPRETATION | Flouda direction/overdot proposals are scholarly interpretation, not canonical physical or linguistic facts. | Exact publication locus and independent assessment of marks and traversal remain needed. |
| ANO-DIS-003 | COUNT_OR_IDENTITY | Malia counts14/15/16 have different segmentation traditions; Chapouthier excludes boundary bars from14. The 16-slot INSCRIBE state is directly described, not a reconciliation of drawings. | Compare specific graphic partitions across sources; never explain14→16 merely by adding the two bars. |
| ANO-DIS-004 | CLASSIFICATION | Stray-find chronology cannot be resolved by a single normalized date. | Preserve each dated authority claim and assess its contextual basis. |
| ANO-DIS-005 | INTERPRETATION | Decipherment proposals remain quarantined hypotheses. | No phonetic adoption without explicit source-specific arguments and independent evaluation. |

`research/attribution-review.json` pins every referenced native artifact by SHA-256 and records exact JSON pointers. `analysis/attribution-review-audit.json` is replayed by the checker. Queries reject changed input bytes before returning any case. The earlier native records remain unchanged.

Pair-attribution states describe documentary limitations, not scientific acceptance. A partial located comparison can be a real scholarly alternative without full typographic, physical-position or independent collation. `NOT_APPLICABLE` marks controls and interpretations for which a two-reading pair is not the appropriate unit. No unknown pair/witness total is replaced with zero.
