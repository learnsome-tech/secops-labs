# IR-0157 post-incident review (blameless), held 2026-03-06

## Why was the bastion login not detected for two days?
1. No rule alerts on a success after repeated failures.
2. Why? bastion01 auth logs never reached the SIEM.
3. Why? bastion01 was built by hand, outside the standard image,
   so log onboarding was skipped.

## Why did a guessed password work at all?
1. PasswordAuthentication was yes on bastion01.
2. Why? The hardening baseline is not checked after a build.

## Why did isolating db01 wait 50 minutes?
1. Isolating a database needed the owner's approval.
2. Why? The SEV1 playbook has no pre-approved containment.

## Actions                                 owner      due    proof
A1 Onboard bastion auth logs to SIEM      platform   03-13  log search
A2 Rule: success after failures           detection  03-13  replay
A3 Enforce sshd baseline after builds     platform   03-20  gate run
A4 Pre-approve SEV1 isolation             ir-lead    03-20  tabletop
