# Editorial spec: employer-facing CV page polish

## Goal

Make the static CV page accurately present Romy's public AI and agent-infrastructure work after the monogram rebrand. Preserve the current visual layout and all existing identity, contact, education, dates, and resume asset decisions.

## User journey

An employer lands on the page, understands Romy's role in one scan, sees public evidence before private or unverified claims, and can follow links to the JEV plugin, merged QQ contribution, Ferrite, Consensus beta, and historical ChatIndex prototype.

## Data and state

The page is a static HTML document. It has no authentication, user accounts, mutable application state, or new durable storage. Existing local assets remain `assets/portrait.png` and `assets/Romy-Mondello-Resume.pdf`.

## Privacy and preservation

Keep the existing public contact links and location text. Do not add private repository names, credentials, provider secrets, or personal data. Do not edit the portrait, resume PDF, repository metadata, or deployment configuration.

## Claim boundaries

Use direct public links for JEV and QQ. Describe Further as co-designed with the CTO. Describe Agent Cloud as a bounded local prototype with explicit cancellation controls and joint development. Label Ferrite, Consensus, and ChatIndex by their current prototype or beta status. Avoid claims of production scale, continuous operation, crash recovery, learned locomotion, trading performance, or hosted acceptance unless the page already has direct public evidence.

## Recovery

The only owned source edit is `index.html`, with checkpoints committed on `codex/cv-polish-20261025`. The change is recoverable through Git. The `.agent-work` spec and verification notes provide the editorial record.

## Acceptance criteria

1. The selected-work order leads with the public JEV plugin and attributable QQ PR #72.
2. Ferrite and Consensus remain represented with accurate public links; ChatIndex may appear only as a labeled historical prototype.
3. Further and Agent Cloud wording matches the claim boundaries above.
4. Existing layout, portrait, resume PDF, contact links, dates, and education remain unchanged.
5. Every external link used in the edited cards resolves to the intended public source, and every local asset reference resolves.
6. The HTML has no broken anchors, duplicate IDs, or unclosed tags detectable by focused static checks.
