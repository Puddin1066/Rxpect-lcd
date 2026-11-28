# RxPect RTM payment precedent and LCD validation

November 28, 2026

## Decision

Start with written interpretation of existing Original Medicare Part B policy in Rhode Island, Jurisdiction K. A new Local Coverage Determination (LCD) is a request to establish local policy. The open question is whether the existing rules allow a claim for monitoring in this workflow. The paid CBT evidence supports asking that question, and a formal LCD request remains an option if the contractor identifies a local coverage gap. Medicare billing should await clarification of the device's regulatory status, coding and coverage.

## What the payment trail proves

CMS Original Medicare fee-for-service, noninstitutional Part B data show payments for CPT 98978, the supply of a device for remote monitoring of cognitive behavioral therapy (CBT). These are published service counts and average Medicare payments, distinct from the allowed amount, which can include cost sharing.

| Year | Beneficiaries | Office services | Average Medicare payment per service |
|---|---:|---:|---:|
| 2023 | 17 | 22 | $29.00 |
| 2024 | 390 | 661 | $37.69 |

| Public rendering practitioner | Location | Year | Services | Average Medicare payment |
|---|---|---:|---:|---:|
| Quentin Shambley, NP | Phoenix, AZ | 2023 | 19 | $27.44 |
| Craig Price, MD | Old Bridge, NJ | 2024 | 210 | $43.12 |
| Sidra Asrar, MD | Jacksonville, FL | 2024 | 126 | $34.11 |
| Justo Cisneros, MD | San Antonio, TX | 2024 | 112 | $34.74 |
| Rispba McCray-Garrison, MD | Houston, TX | 2024 | 109 | $36.47 |
| Susan Mendelsohn, PsyD | Fort Lauderdale, FL | 2024 | 26 | $37.18 |

The five 2024 public practitioner rows account for 583 of the 661 national services. CMS suppresses small counts, so the practitioners listed are an incomplete roster. The public data aggregate payments by code and rendering practitioner. They contain no app name, case-level records, linked therapy claim, payer for the CBT itself, or clinical rationale. The claims demonstrate that Medicare paid the CBT device-supply code in practice. No paid case has been reconstructed at the product or clinical workflow level.

Reproduce by filtering `HCPCS_Cd=98978` through the CMS API using `filter[HCPCS_Cd]`. Use the national office row in the geography file and report `Tot_Benes`, `Tot_Srvcs`, and `Avg_Mdcr_Pymt_Amt`.

- [2024 geography query](https://data.cms.gov/data-api/v1/dataset/0c75b0b3-b40f-4007-a5ac-f9f2fed95862/data?filter%5BHCPCS_Cd%5D=98978)
- [2023 geography query](https://data.cms.gov/data-api/v1/dataset/ddee9e22-7889-4bef-975a-7853e4cd0fbb/data?filter%5BHCPCS_Cd%5D=98978)
- [2024 provider query](https://data.cms.gov/data-api/v1/dataset/92396110-2aed-4d63-a6a2-5d6207d46a29/data?filter%5BHCPCS_Cd%5D=98978)
- [2023 provider query](https://data.cms.gov/data-api/v1/dataset/0e9f2f2b-7bf9-451a-912c-e02e654dd725/data?filter%5BHCPCS_Cd%5D=98978)
- [CMS methodology](https://www.cms.gov/newsroom/fact-sheets/new-medicare-data-available-increase-transparency-physician-utilization)

## How the precedent applies

| Scenario | Underlying intervention | Service for which payment is sought | Evidence |
|---|---|---|---|
| CBT | CBT regimen | Supply of a device to monitor CBT | Paid 98978 services in Original Medicare |
| Lumbar exercise | Home exercise under a PT plan | Musculoskeletal RTM device supply and applicable clinician management | Existing MSK codes, subject to eligibility and medical necessity |
| RxPect | Separately funded investigational open-label placebo (OLP) adjunct | Monitoring adherence, symptoms and function used to manage covered PT | Specific workflow needs written interpretation |

CBT and lumbar exercise payment may occur separately. An RTM payment by itself establishes only what monitoring service was billed and paid. The same app could deliver an intervention and collect data. Whether Medicare pays when that workflow includes an investigational adjunct remains the open question. For 2026, the proposed code families to ask about are 98985/98977 for musculoskeletal device supply and 98979/98980/98981 for qualifying treatment management. Device status, monitoring medical necessity, code requirements and the covered PT plan each matter. CMS finalized national pricing for the CBT supply codes for 2027, which does not resolve RxPect eligibility.

SleepioRx is a product design analogue. The FDA summary describes digital CBT for insomnia with daily sleep tracking and a provider dashboard. Big Health publishes a digital mental health treatment billing pathway. Highmark Pennsylvania's commercial policy names RelieVRx for chronic low back pain and lists musculoskeletal and CBT RTM codes among several policy codes. Its tables do not establish a paid product-to-code match. Medicare classifies the RelieVRx-specific E1905 code as durable medical equipment.

- [CMS 2026 therapy code update](https://www.cms.gov/files/document/mm14250-therapy-code-list-2026-annual-update.pdf)
- [CMS 2027 final rule](https://www.govinfo.gov/content/pkg/FR-2026-11-09/pdf/2026-22743.pdf)
- [FDA Sleepio decision summary](https://www.accessdata.fda.gov/cdrh_docs/pdf23/K233577.pdf)
- [Big Health billing guidance](https://www.bighealth.com/faqs)
- [Highmark prescription digital therapeutics policy](https://securecms.highmark.com/content/medpolicy/en/highmark/pa/commercial/policies/Miscellaneous/Z-105/Z-105-007.html)
- [CMS DME classification](https://www.cms.gov/files/document/r13774bp.pdf)

## What would validate the RxPect workflow

Wellpoint's November 23 educational response expressed concerns about coverage of placebo and FDA status. A November 28 follow-up already asked separately about RTM device supply, treatment management, the governing device provisions, and the LCD route. Add the CBT evidence to that existing thread when it advances the inquiry. Treat written guidance as policy interpretation and distinguish it from an individual claim determination.

1. Obtain a written answer for the same covered PT plan and monitoring workflow with home exercise as the reference case and separately funded OLP as the comparison. Ask whether the latter is independently disqualifying, what provision controls, and whether individual medical necessity can be assessed.
2. Where an existing LCD or billing article controls, obtain the specific restriction and ask whether reconsideration or another policy route applies. Check L33631 and A56566 with the contractor.
3. If Wellpoint identifies a need for new local policy, use A56198 and establish that the request addresses monitoring. Assemble evidence that the data change PT management, with a comparator such as usual PT or PT without the monitoring. Trials of OLP efficacy answer a different question. If the barrier is national coding, benefit authority, or device regulatory status, ask for the controlling rule and appropriate pathway.
4. Any actual claim should reflect care furnished to a patient with appropriate documentation and a verified billing basis. A paid case verifies that case and its circumstances.

- [A56198 current new LCD request process](https://www.cms.gov/medicare-coverage-database/view/article.aspx?Cntrctr=275&articleId=56198)
- [L33631 outpatient PT and OT](https://www.cms.gov/medicare-coverage-database/view/lcd.aspx?LCDId=33631)
- [A56566 billing and coding](https://www.cms.gov/medicare-coverage-database/view/article.aspx?articleId=56566)

## Three proposed emails

### 1. Craig Price, MD, via the practice billing manager

Verified public practice-location route: [42 Throckmorton Lane office](https://www.getcare.hackensackmeridianhealth.org/en/locations/hmh-primary-care-old-bridge-42-throckmorton-lane), 732-607-1111. The public office roster does not currently list Dr. Price. Ask the office to verify the correct billing contact before addressing the message. A direct work email was not verified.

**Subject**  
Question about the monitoring device used for Medicare CPT 98978

Hello, I’m John Round with RxPect. CMS’s public 2024 data list Dr. Craig Price as the rendering practitioner for Medicare CBT monitoring device supply under 98978. Could the billing team confirm the device or app name and whether it delivered the CBT or tracked a program delivered elsewhere? It would help to know whether the underlying therapy was billed separately or provided through another arrangement. Confirmation for one Medicare-paid example in general terms would be plenty. Please omit patient information.

### 2. Susan Mendelsohn, PsyD, via Fort Lauderdale Psychology Group

Verified route: [practice contact form](https://transformempowersoar.com/contact-us.html) or 954-294-7036 to obtain the practice billing email. A direct work email was not verified.

**Subject**  
How CBT monitoring worked in your Medicare practice

Dr. Mendelsohn, I’m researching how Medicare pays for remote monitoring of a behavioral intervention. CMS’s public 2024 data show payments under CPT 98978 associated with your practice. Would you or your biller be willing to describe one example in general terms? I’m trying to establish what CBT the patient did, which app captured adherence or response, what you did with the data, and whether the CBT itself was billed separately, self-paid, or provided without a separate charge. Please omit patient information.

### 3. Wellpoint Federal, existing Jurisdiction K Part B POE and Medical Policy thread

The November 28 follow-up is already on the thread. Use the language below when the contractor replies or as an evidence supplement if it remains unanswered.

**Subject**  
Re: Jurisdiction K inquiry on RTM for chronic low back pain

Thank you for reviewing our inquiry. CMS public fee-for-service data show 661 services in 2024 under CPT 98978, which pays for supplying a CBT monitoring device. We cite this as evidence of payment for monitoring a behavioral intervention. In the workflow already described, an enrolled PT would use musculoskeletal monitoring data to manage a covered chronic low back pain plan while a separately funded investigational open-label placebo adjunct is used at home. Does that adjunct independently bar payment for device supply or treatment management under current policy? Please identify the controlling provision and advise whether the question can be evaluated under existing policy on individual medical necessity or requires an LCD request or reconsideration. If you need an enrolled Rhode Island PT practice to submit the scenario, please direct us to the appropriate channel.

## What would close the evidence gap

Provider confirmation should link a named product, therapy delivery and funding, monitored measurements, and at least one paid 98978 service. A written practice confirmation or a voluntarily supplied fully de-identified remittance paired with a workflow description would strengthen that link. Wellpoint's response should identify a controlling provision and specify whether existing policy, LCD reconsideration, a new LCD, or a national requirement governs RxPect.
