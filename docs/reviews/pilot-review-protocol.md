# Pilot semantic review protocol

The 78 Unisermo/English pairs are draft translations. Parser validity does not establish semantic equivalence.

For each pair, independently assess person, number, tense, aspect, arguments, case, definiteness, reference, negation, modality, and ambiguity. Record a verdict of `pending`, `needs_revision`, `verified`, or `rejected`, an explanation, and reviewer attribution. Automated checks may identify problems but cannot by themselves approve a translation.

Never overwrite the original benchmark evidence. If any translation changes, version the corpus and rerun the tokenizer measurement using its new fingerprint. Freeze evaluation holdouts before tuning linguistic forms.

Expanded corpus targets and original pilot evidence are documented in [LDR-0007](../ldr/LDR-0007-tokenization-diagnostic-baseline.md).
