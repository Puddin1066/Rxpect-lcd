# RxPect RTM payment precedent and coverage validation

28 November 2026 | Original Medicare Part B | Research and outreach drafts

## Decision

Start with a written Jurisdiction K interpretation under existing rules. CMS says MACs review claims individually when no LCD or NCD applies. Keep the LCD draft in reserve while Wellpoint determines whether monitoring this specific intervention can be reviewed under current policy. The question is whether the investigational, separately funded OLP adjunct itself precludes qualifying musculoskeletal RTM supply or treatment management within covered outpatient PT. Clarify each code family separately. An LCD can address local coverage within national rules. Use reconsideration if an existing LCD provision needs revision, and the new LCD process if a distinct local policy is warranted. A national restriction requires analysis of the controlling CMS rule.

## Verified payment trail

Queried the CMS Physician & Other Practitioners Geography and Service API for HCPCS 98978 and used its national rows. Dollar values are the published average Medicare payment per service, rounded to cents. These are historical observed averages, separate from current fee schedules.

| Year | Beneficiaries | Services | Average Medicare payment |
|---|---:|---:|---:|
| 2023 | 17 | 22 | $29.00 |
| 2024 | 390 | 661 | $37.69 |

From the 2024 Provider and Service API, filtered to HCPCS 98978:

| Rendering practitioner | NPI | CMS specialty | Beneficiaries | Services | Avg. payment |
|---|---|---|---:|---:|---:|
| Craig Price | 1851313845 | Internal Medicine | 120 | 210 | $43.12 |
| Sidra Asrar | 1508353962 | Pediatric Medicine | 76 | 126 | $34.11 |
| Justo Cisneros | 1427168061 | Internal Medicine | 63 | 112 | $34.74 |
| Rispba McCray-Garrison | 1164613352 | General Practice | 71 | 109 | $36.47 |
| Susan Mendelsohn | 1669531596 | Clinical Psychologist | 12 | 26 | $37.18 |

The five published provider rows total 583 services. CMS aggregates by rendering NPI, code and place of service and redacts small cells. These files cannot identify a device brand, individual encounters, same-patient services, line-level modifiers, or who paid for the underlying CBT.

Filtering the same 2024 provider API by NPI shows Price also had 460 units of 98975, 1,594 of 98977, 2,310 of 98980 and 1,022 of 98981. Mendelsohn also had 587 units of psychotherapy code 90837 and 30 of 98980. These are provider-year co-occurrences. They are compatible with separate treatment and monitoring activity at a practice, but cannot establish co-billing for a patient or an episode.

## What the precedent supports

- Medicare paid for supplying a device to monitor CBT under 98978. The object of that payment is the monitoring supply. The payment records leave open whether CBT itself was covered, paid separately, built into the device, sponsor-funded, or furnished without a separate charge.
- A prescribed exercise and an app-delivered therapy each provide a specific activity whose adherence or response can be monitored. RxPect's app may be necessary for delivering its particular protocol as designed and for collecting and transmitting monitoring data. That dual function is a useful analogy. Coverage still turns on whether the monitoring qualifies, including the device and its intended use, whether the code reflects what is actually monitored, and whether the therapist uses the data in skilled clinical care.
- RelieVRx is a product-level comparator for chronic low-back pain. CMS specifically created E1905 and classified the product under DME. A historical Highmark Pennsylvania commercial policy names EaseVRx and other digital therapies alongside a shared 98978 code list and separately states a position on E1905. Neither establishes an actual RelieVRx RTM payment. Keep commercial coverage and Original Medicare evidence distinct.
- The closest desired comparator is a paid Original Medicare RTM episode with a verified device, a therapy delivered by or used alongside that device, and an identified funding source for the therapy. Stronger still would be same-app delivery and monitoring with no separate Medicare payment for the intervention. Even that would be an analogy, since CBT and musculoskeletal RTM use different supply codes and the investigational OLP question remains open.

## Reconstruct one paid episode

Ask a billing contact for a de-identified **summary**, omitting patient identifiers, dates tied to an individual, claim numbers, and raw remittances. Capture payer and year, paid RTM code and actual payment status, type or name of device, therapy and who furnished it, whether the same device delivered and monitored it, what the device captured, who paid for the underlying treatment, any accompanying management code, clinical use of the data, and whether any unusual program or contractual arrangement governed payment. A provider attestation that their billing team checked a paid remittance adds stronger support than a recollection or coding recommendation. The public files alone cannot reconstruct an episode.

## Three inquiries

### 1. Wellpoint Federal Part B POE, with Medical Policy copied

Use the existing thread and the November 28 inquiry. Send this addition after a substantive response or when a follow-up is due, so the comparator links directly to the open question.

**Subject** Re: Jurisdiction K inquiry on musculoskeletal RTM for chronic low back pain

> Hello Wellpoint team,
>
> One comparator may help isolate our question. CMS's Original Medicare data show actual payment under 98978 for CBT monitoring device supply. The public data leave the underlying therapy's financing open. Our question concerns the corresponding musculoskeletal monitoring pathway for a Rhode Island PT treating chronic nonspecific low back pain, where the same app delivers and monitors a fully disclosed, separately funded investigational open-label placebo adjunct.
>
> Assuming the device, practitioner and services otherwise qualify, does the investigational adjunct itself preclude payment for 98985/98977 supply or 98979/98980/98981 management? Could each be reviewed for medical necessity under current policy? If either is barred, please identify the governing provision. If a local policy change is necessary, should we seek reconsideration of an existing LCD or a new LCD? Could you route this to Medical Policy and share a reference number if one has been assigned?
>
> Thank you,  
> John Round | Biotica Bio / RxPect

### 2. Dr. Susan Mendelsohn or practice billing lead

Use the practice's public contact form to request routing to billing or a professional email. Craig Price's practice is a backup with the largest observed 98978 volume and substantial musculoskeletal RTM volume. No direct professional email was verified for either practice.

**Subject** Brief question about a paid Medicare CBT monitoring workflow

> Hello Dr. Mendelsohn,
>
> I'm researching how clinicians use CBT monitoring in practice. CMS's public 2024 data show your practice furnished services under 98978. Could you or your billing lead confirm, from one paid Original Medicare example, which device or app was supplied, whether it delivered the CBT as well as monitoring it, and whether the CBT itself was separately billed or funded?
>
> If you can confirm whether a management code was also paid for that episode, that would help. A brief workflow-level summary is plenty. Please omit patient information and claim documents.
>
> Thank you,  
> John Round | Biotica Bio / RxPect

### 3. AppliedVR reimbursement or market access team

Route via the published corporate contact, info@appliedvr.io.

**Subject** Has Original Medicare paid RTM for a RelieVRx workflow?

> Hello AppliedVR team,
>
> Could you route this to reimbursement or market access? CMS created E1905 for RelieVRx. I'm trying to verify whether any clinician also received an actual Original Medicare payment for RTM device supply or treatment management involving a RelieVRx patient.
>
> If so, could you share the paid RTM code, payer type and year, what data the clinician used, and whether the program itself was funded through E1905, another payer, or separately from the RTM service? A de-identified workflow summary or public reference would be sufficient. A commercial example would also be useful if labeled as such.
>
> Thank you,  
> John Round | Biotica Bio / RxPect

## Reproducible sources

- [2023 CMS 98978 geography rows](https://data.cms.gov/data-api/v1/dataset/ddee9e22-7889-4bef-975a-7853e4cd0fbb/data?filter%5BHCPCS_Cd%5D=98978&size=30)
- [2024 CMS 98978 geography rows](https://data.cms.gov/data-api/v1/dataset/0c75b0b3-b40f-4007-a5ac-f9f2fed95862/data?filter%5BHCPCS_Cd%5D=98978&size=30)
- [2024 CMS 98978 provider rows](https://data.cms.gov/data-api/v1/dataset/92396110-2aed-4d63-a6a2-5d6207d46a29/data?filter%5BHCPCS_Cd%5D=98978&size=30). To reproduce the NPI cross-check, replace the code filter with filter%5BRndrng_NPI%5D and the selected NPI.
- [CMS methodology](https://data.cms.gov/sites/default/files/2024-06/MUP_PHY_RY24_20240530_Methodology_508_0.pdf)
- [CMS RTM codes](https://www.cms.gov/medicare/payment/fee-schedules/physician-fee-schedule/care-management/transitional-care-management-services) and [2026 therapy coding instructions](https://www.cms.gov/files/document/mm14250-therapy-code-list-2026-annual-update.pdf). Use rules for the service year and confirm code fit for the actual workflow.
- [CMS coverage and claim-by-claim review](https://www.cms.gov/cms-guide-medical-technology-companies-and-other-interested-parties/coverage/medicare-coverage-items-and-services), [Wellpoint outpatient therapy LCD L33631](https://www.cms.gov/medicare-coverage-database/view/lcd.aspx?LCDId=33631), and [new LCD process A56198](https://www.cms.gov/medicare-coverage-database/view/article.aspx?articleid=56198)
- [CMS E1905 determination](https://www.cms.gov/files/document/2022-hcpcs-application-summary-biannual-2-2022-non-drug-and-non-biological-items-and-services.pdf) and [historical Highmark commercial policy](https://securecms.highmark.com/content/medpolicy/en/highmark/pa/commercial/policies/Miscellaneous/Z-105/Z-105-004.html)
- [Mendelsohn practice contact](https://transformempowersoar.com/contact-us.html), [Price practice directory](https://find-doctor.ama-assn.org/doctor/craig-charles-price-md/6783110), and [AppliedVR contact](https://www.appliedvr.io/contact)
