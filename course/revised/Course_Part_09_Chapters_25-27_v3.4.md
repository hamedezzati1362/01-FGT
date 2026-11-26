# Enterprise Network & Security Engineering — دوره‌ی تخصصی Cisco و Enterprise Firewall
## بخش ۹ از ۱۱ — فصل‌های ۲۵ تا ۲۷

| مورد | مقدار |
|---|---|
| نام دوره | Enterprise Network & Security Engineering (Cisco + FortiGate) |
| شماره بخش | ۹ از ۱۱ |
| فصل‌های این فایل | ۲۵ ، ۲۶ ، ۲۷ |
| تاریخ تولید | ۲۰۲۶-۱۱-۲۶ |
| نسخه Blueprint | v3.0 (+ بازبینی ۱٫۱) |
| نسخه‌های نرم‌افزار | FortiOS 7.0.3 (اسمی؛ بوت‌نشده؛ تأیید با `get system status`) ؛ Cisco vIOS-L2 15.2(20200924، Experimental) ؛ Cisco vIOS 15.9(3)M9 ؛ VPCS ؛ PNetLab 4.2.8 ؛ ESXi 8.0U2 ؛ CSR1000v 17.03.02 (IOS-XE؛ آزمایش‌نشده) |
| وضعیت تکمیل | **فصل‌های ۲۵–۲۷ تولید شد؛ Multi-vendor، FMG/FAZ و جایگزین، Logging/Monitoring/API/Hardening.** Labها «اجرا نشده»؛ FMG/FAZ Needs-License؛ دستورها آزمایش‌نشده. |

> **قوانین خواندن:** تمرین‌ها و پرسش‌های مرور بدون پاسخ‌اند؛ پاسخ در «پاسخ‌های فصل». «اجرا نشده» یعنی خروجی‌ها **پیش‌نیاز/پیش‌بینی** هستند. «CLI-Accepted» ≠ «کار می‌کند». رمزها نمونه‌اند.

### وضعیت راستی‌آزمایی Labهای این بخش
خلاصه: اجرا نشده (فقط طراحی): 13.

| Lab | وضعیت |
|---|---|
| 25-1 | اجرا نشده (فقط طراحی) |
| 25-2 | اجرا نشده (فقط طراحی) |
| 25-3 | اجرا نشده (فقط طراحی) |
| 25-4 | اجرا نشده (فقط طراحی) |
| 26-1 | اجرا نشده (فقط طراحی) |
| 26-2 | اجرا نشده (فقط طراحی) |
| 26-3 | اجرا نشده (فقط طراحی) |
| 26-4 | اجرا نشده (فقط طراحی) |
| 27-1 | اجرا نشده (فقط طراحی) |
| 27-2 | اجرا نشده (فقط طراحی) |
| 27-3 | اجرا نشده (فقط طراحی) |
| 27-4 | اجرا نشده (فقط طراحی) |
| 27-5 | اجرا نشده (فقط طراحی) |

---

<a id="ch25"></a>

> **نسخه v3.4:** این بخش در دسته‌های B/A/C بدون تغییر محتوایی است (فشرده‌تر از فصل‌های توسعه‌یافته؛ در دسته D بازنویسی می‌شود).

# فصل 25 — Multi-Vendor: FortiGate در کنار Cisco CSR (معماری ۶)

**مدت:** ۳۶ ساعت | **پیش‌نیاز:** فصل ۹، ۱۸، ۱۹.
**اهداف:** اتصال FGT و CSR با BGP/OSPF؛ IPsec چندسازنده؛ تفاوت Terminology؛ Troubleshooting مقایسه‌ای.
**نسخه:** CSR1000v 17.03.02 (IOS-XE) و FortiOS 7.0.3 اسمی؛ آزمایش‌نشده.
**اشتباهات رایج:** پیش‌فرض‌های ناهمسان (Timer، MTU، Lifetime)؛ Router-ID؛ اختلاف Passive-interface.

**درس‌های فصل:**
- [درس 25-1 — تفاوت اصطلاحات Cisco و Fortinet](#l-25-1)
- [درس 25-2 — BGP/OSPF بین FGT و CSR](#l-25-2)
- [درس 25-3 — IPsec چندسازنده و عیب‌یابی مقایسه‌ای](#l-25-3)
- [درس 25-4 — معماری ۶ و آزمون](#l-25-4)

---

<a id="l-25-1"></a>

## درس 25-0 — Interoperability چندسازنده: نگاشت مفاهیم، پیش‌فرض‌های ناهمسان و عیب‌یابی

**فصل ۲۵ · درس افزوده (پیش‌درس ۲۵-۱) · پیش‌نیاز: ۱۸-۰، ۵-۷، ۹-۷ · ≈ ۵ ساعت**

> **وضعیت:** CSR1000v 17.03.02 (IOS-XE) و FortiOS 7.0.3؛ دستورهای CSR/FortiGate `Unverified`؛ Lab «اجرا نشده».

### ۱) هدف آموزشی

1. نگاشت اصطلاحات Cisco و Fortinet (Interface، Zone، ACL/Policy، Route-map، VRF/VDOM).
2. شناخت **پیش‌فرض‌های ناهمسان** و آثار آن (Timer، MTU، Lifetime، Authentication).
3. اتصال Cisco–FortiGate با OSPF/BGP و IPsec و عیب‌یابی مقایسه‌ای.
4. نوشتن چک‌لیست Interop.

### ۲) مفهوم پایه

پروتکل‌ها استاندارد (RFC) هستند ولی **پیش‌فرض‌ها و محدودیت‌ها** برند-به-برند فرق دارد؛ بیشتر خرابی Interop از «فرض یکسان بودن پیش‌فرض‌ها» می‌آید.

### ۳) توضیح عمیق فنی

#### ۳-۱) نگاشت مفاهیم

| مفهوم | Cisco IOS-XE | FortiOS |
|---|---|---|
| Interface L3 | `interface Gi0/1` + `ip address` | `config system interface` |
| Zone | (Zone-Based Firewall) | `config system zone` |
| ACL/Policy | ACL | Firewall Policy |
| NAT | `ip nat` | Policy NAT/VIP/IP Pool |
| Route-map | `route-map` | `config router route-map` |
| Prefix-list | `ip prefix-list` | `config router prefix-list` |
| VRF | `vrf` | VDOM/VRF |
| نمایش جدول مسیر | `show ip route` | `get router info routing-table all` |
| نمایش Session | `show ip nat translations` | `diagnose sys session list` |

#### ۳-۲) پیش‌فرض‌های ناهمسان (نمونه)

| مورد | Cisco | FortiOS | اثر |
|---|---|---|---|
| OSPF Hello/Dead | 10/40 (Broadcast/P2P) | قابل‌تنظیم؛ باید یکی باشد | Neighbor نمی‌آید |
| OSPF Network Type | Broadcast روی Ethernet | تنظیم دستی | DR/BDR یا P2P ناسازگار |
| MTU | 1500 | 1500؛ Tunnel کمتر | OSPF Exstart |
| IKEv2 | قابل‌تنظیم | IKEv1 پیش‌فرض در 7.0 (CLI Ref) | عدم توافق |
| PFS | Group تنظیم | PFS پیش‌فرض enable | Phase 2 ناسازگار |
| Lifetime | IKE 24h، IPsec 1h (پیش‌فرض‌های متداول؛ `Unverified`) | 86400/43200 | Rekey ناهمسان |
| BGP Hold | 180 | 180 (متداول؛ `Unverified`) | — |

(جدول بر پایه‌ی پیش‌فرض‌های متداول است؛ هر مقدار را در Lab بخوانید.)

#### ۳-۳) استراتژی Interop

1. هر دو سمت را **صریح** پیکربندی کنید؛ به پیش‌فرض‌ها تکیه نکنید.
2. یک «برگه‌ی پارامتر» مشترک (Proposal، DH، PFS، Timer، MTU، MSS، Auth).
3. تست مرحله‌ای: L3 → Routing → IPsec → Policy.
4. عیب‌یابی با Debug **هر دو سو** هم‌زمان.

### ۴) مثال حل‌شده

**OSPF FGT–CSR:** Neighbor در Exstart می‌ماند. شواهد: `show ip ospf neighbor` (CSR) Exstart؛ `get router info ospf neighbor` (FGT). **علت:** MTU متفاوت (Tunnel/VLAN). **رفع:** MTU یکسان یا `ip ospf mtu-ignore` (CSR؛ با ریسک؛ `Unverified`). **تأیید:** Full.

``` text
! CSR
interface Tunnel0
 ip mtu 1400
 ip ospf network point-to-point
router ospf 1
 network 10.255.0.0 0.0.0.3 area 0
```

``` text
# FortiGate
config router ospf
    config ospf-interface
        edit "TO-CSR"
            set interface "TO-CSR"
            set network-type point-to-point
        next
    end
end
```

**IPsec Interop (مثال سخت):** Phase 1 OK، Phase 2 NO_PROPOSAL_CHOSEN. فرضیه‌ها: PFS/DH Group، Transform، Selector. شاهد: Debug هر دو؛ **رفع:** تطبیق PFS Group و Proposal.

### ۵) GUI و CLI

FortiGate: Network → OSPF/BGP؛ VPN → IPsec Tunnels. CSR: CLI. **Verification:** `show ip ospf neighbor`/`get router info ospf neighbor`؛ `show crypto ikev2 sa`/`diagnose vpn ike gateway list`.

### ۶) نکات امنیتی

- Authentication OSPF/BGP هر دو سمت یکسان.
- از الگوریتم‌های قوی مشترک.

### ۷) جمع‌بندی

- پروتکل یکی؛ پیش‌فرض‌ها فرق دارد.
- پیکربندی صریح + برگه‌ی پارامتر.
- Debug دو سمتی.

### ۸) تمرین و ارزیابی

**ت1.** (ساده) معادل `show ip route` در FortiOS؟ *(پاسخ: 25-0-ت1)*

**ت2.** (متوسط) چرا OSPF در Exstart می‌ماند؟ *(پاسخ: 25-0-ت2)*

**ت3.** (سخت) یک برگه‌ی پارامتر IPsec بین FGT و CSR بنویسید. *(پاسخ: 25-0-ت3)*

**Q1.** Quick quiz (English): Why shouldn't you rely on vendor defaults in multi-vendor links? *(پاسخ: 25-0-Q1)*

### ۹) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Interop | Interoperability | سازگاری |
| Exstart | OSPF ExStart state | مرحله‌ی تبادل DBD |
| mtu-ignore | OSPF MTU ignore | نادیده‌گرفتن MTU |

- *Configure parameters explicitly on both vendors.* ← پارامترها را روی هر دو سازنده صریحاً تنظیم کنید.

### ۱۰) منابع

- Cisco: IOS XE OSPF/IKEv2 Configuration Guides؛ Fortinet Docs: FortiOS 7.0 CLI Reference (`config router ospf`، `phase1-interface`)؛ RFC 2328، RFC 7296.

## درس 25-1 — تفاوت اصطلاحات Cisco و Fortinet

**فصل 25 - روز 1 · پیش‌نیاز: فصل ۲۴ · ۶ ساعت**

### ۱) معرفی درس

جدول معادل‌ها قبل از پیکربندی.

### ۲) پیش‌نیازها

فصل ۲۴

### ۳) توضیح مفهومی

- VLAN Interface در برابر SVI.
- Zone در برابر Security-level.
- Policy در برابر ACL+NAT.
- Route-map در برابر Route-map/Prefix-list.
- Show در برابر get/diagnose.

### ۴) مثال ساده

دو برند باید با هم صحبت کنند.

### ۵) مثال سازمانی

سازمان: لبه Fortinet و هسته Cisco.

### ۶) تصویر و توپولوژی

```text
CSR (core) <-BGP-> FGT (edge)
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. Network > Static Routes (FGT).

#### روش خط فرمان (CLI)

```text
show ip route
get router info routing-table all
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- خواندنی؛ هر دو.

### ۸) تست عملکرد

- جدول معادل را کامل کنید.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | دستور اشتباه |
| شواهد/دستور | خطا |
| علت | Syntax برند |
| رفع | معادل |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** get؟ *(پاسخ: 25-1-ت1)*

**ت2.** ACL؟ *(پاسخ: 25-1-ت2)*

### ۱۱) مرور و ارزیابی

**م1.** چرا جدول؟ *(پاسخ: 25-1-م1)*

**م2.** سناریو: show در FGT؛ چه؟ *(پاسخ: 25-1-م2)*

**معیار تسلط:** اتصال دوبرندی.

**اشتباهات رایج:** پیش‌فرض‌های ناهمسان.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| SVI | Switch Virtual Interface | Interface مجازی | Cisco |

| English sentence | ترجمه |
|---|---|
| Keep a vendor command cheat sheet. | یک برگه‌ی تطبیق دستورها نگه دارید. |

#### کارت Lab — درس 25-1

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | جدول معادل |
| 2 | پیش‌نیاز | فصل ۲۴ |
| 3 | توپولوژی | CSR+FGT |
| 4 | تجهیزات | — |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | — |
| 7 | وضعیت اولیه | — |
| 8 | صورت مسئله | جدول |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | — |
| 11 | سناریوی خرابی | دستور اشتباه |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | سند |
| 14 | معیار پذیرش | تأیید |
| 15 | مستندات نهایی | `02-design/vendor-map.md` |
| 16 | Cleanup و بازگردانی | — |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="l-25-2"></a>

## درس 25-2 — BGP/OSPF بین FGT و CSR

**فصل 25 - روز 2 · پیش‌نیاز: درس ۲۵-۰ · ۶ ساعت**

### ۱) معرفی درس

Routing مشترک.

### ۲) پیش‌نیازها

درس ۲۵-۰

### ۳) توضیح مفهومی

- OSPF: Area/Network Type/Hello.
- BGP: AS/Neighbor.
- Timer و Authentication هماهنگ.
- Route-map.
- Verification دوطرفه.

### ۴) مثال ساده

دو برند باید با هم صحبت کنند.

### ۵) مثال سازمانی

سازمان: لبه Fortinet و هسته Cisco.

### ۶) تصویر و توپولوژی

```text
CSR (core) <-BGP-> FGT (edge)
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. Network > OSPF (FGT).

#### روش خط فرمان (CLI)

```text
! CSR
router ospf 1
 network 10.0.0.0 0.0.0.255 area 0
! FGT
get router info ospf neighbor
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- `Unverified`.

### ۸) تست عملکرد

- Neighbor Full.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | Neighbor Exstart |
| شواهد/دستور | `ospf neighbor` |
| علت | MTU mismatch |
| رفع | MTU یکسان |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** Exstart؟ *(پاسخ: 25-2-ت1)*

**ت2.** Timer؟ *(پاسخ: 25-2-ت2)*

### ۱۱) مرور و ارزیابی

**م1.** چرا MTU؟ *(پاسخ: 25-2-م1)*

**م2.** سناریو: Exstart؛ علت؟ *(پاسخ: 25-2-م2)*

**معیار تسلط:** اتصال دوبرندی.

**اشتباهات رایج:** پیش‌فرض‌های ناهمسان.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| DBD | Database Description | بسته‌ی OSPF | OSPF |

| English sentence | ترجمه |
|---|---|
| Match MTU on both sides. | MTU را دو طرف یکسان کنید. |

#### کارت Lab — درس 25-2

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | OSPF FGT-CSR |
| 2 | پیش‌نیاز | درس ۲۵-۰ |
| 3 | توپولوژی | FGT+CSR |
| 4 | تجهیزات | FGT+CSR |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | — |
| 7 | وضعیت اولیه | Baseline |
| 8 | صورت مسئله | OSPF |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | show/get |
| 11 | سناریوی خرابی | Neighbor Exstart |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | Full |
| 14 | معیار پذیرش | ثبت |
| 15 | مستندات نهایی | `03-ops/ospf-fgt-csr.md` |
| 16 | Cleanup و بازگردانی | حذف |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="l-25-3"></a>

## درس 25-3 — IPsec چندسازنده و عیب‌یابی مقایسه‌ای

**فصل 25 - روز 3 · پیش‌نیاز: درس ۲۵-۱ · ۶ ساعت**

### ۱) معرفی درس

Interop IPsec.

### ۲) پیش‌نیازها

درس ۲۵-۱

### ۳) توضیح مفهومی

- Proposal/DH/Lifetime.
- IKEv2.
- Selector.
- Debug هر دو سو.
- Evidence.

### ۴) مثال ساده

دو برند باید با هم صحبت کنند.

### ۵) مثال سازمانی

سازمان: لبه Fortinet و هسته Cisco.

### ۶) تصویر و توپولوژی

```text
CSR (core) <-BGP-> FGT (edge)
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. Monitor > IPsec.

#### روش خط فرمان (CLI)

```text
show crypto ikev2 sa
diagnose vpn ike gateway list
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- `Unverified`.

### ۸) تست عملکرد

- Tunnel Up.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | Phase 2 شکست |
| شواهد/دستور | Debug |
| علت | Selector |
| رفع | تطبیق |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** Interop؟ *(پاسخ: 25-3-ت1)*

**ت2.** Debug؟ *(پاسخ: 25-3-ت2)*

### ۱۱) مرور و ارزیابی

**م1.** چرا هر دو سو؟ *(پاسخ: 25-3-م1)*

**م2.** سناریو: یک‌طرفه؛ علت؟ *(پاسخ: 25-3-م2)*

**معیار تسلط:** اتصال دوبرندی.

**اشتباهات رایج:** پیش‌فرض‌های ناهمسان.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| Interop | Interoperability | سازگاری | Multi-vendor |

| English sentence | ترجمه |
|---|---|
| Debug both ends together. | هر دو سر را با هم Debug کنید. |

#### کارت Lab — درس 25-3

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | IPsec FGT-CSR |
| 2 | پیش‌نیاز | درس ۲۵-۱ |
| 3 | توپولوژی | FGT+CSR |
| 4 | تجهیزات | FGT+CSR |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | — |
| 7 | وضعیت اولیه | Baseline |
| 8 | صورت مسئله | Tunnel |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | show |
| 11 | سناریوی خرابی | Phase 2 شکست |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | Up |
| 14 | معیار پذیرش | ثبت |
| 15 | مستندات نهایی | `03-ops/ipsec-mv.md` |
| 16 | Cleanup و بازگردانی | حذف |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="l-25-4"></a>

## درس 25-4 — معماری ۶ و آزمون

**فصل 25 - روز 4 · پیش‌نیاز: درس ۲۵-۲ · ۶ ساعت**

### ۱) معرفی درس

ترکیب و ارزیابی.

### ۲) پیش‌نیازها

درس ۲۵-۲

### ۳) توضیح مفهومی

- اتصال کامل.
- Failover.
- RCA.
- Backup.
- آزمون.

### ۴) مثال ساده

دو برند باید با هم صحبت کنند.

### ۵) مثال سازمانی

سازمان: لبه Fortinet و هسته Cisco.

### ۶) تصویر و توپولوژی

```text
CSR (core) <-BGP-> FGT (edge)
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. Monitor.

#### روش خط فرمان (CLI)

```text
show running-config | section router
get router info routing-table all
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- خواندنی.

### ۸) تست عملکرد

- اجرای A6.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | مسیر نامتقارن |
| شواهد/دستور | traceroute |
| علت | Metric |
| رفع | تنظیم |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** A6؟ *(پاسخ: 25-4-ت1)*

**ت2.** Backup؟ *(پاسخ: 25-4-ت2)*

### ۱۱) مرور و ارزیابی

**م1.** چرا RCA؟ *(پاسخ: 25-4-م1)*

**م2.** سناریو: Route نیست؛ علت؟ *(پاسخ: 25-4-م2)*

**معیار تسلط:** اتصال دوبرندی.

**اشتباهات رایج:** پیش‌فرض‌های ناهمسان.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| A6 | Architecture 6 | معماری ۶ | دوره |

| English sentence | ترجمه |
|---|---|
| Back up both vendors. | از هر دو سازنده Backup بگیرید. |

#### کارت Lab — درس 25-4

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | آزمون A6 |
| 2 | پیش‌نیاز | درس ۲۵-۲ |
| 3 | توپولوژی | FGT+CSR |
| 4 | تجهیزات | FGT+CSR |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | — |
| 7 | وضعیت اولیه | Baseline |
| 8 | صورت مسئله | A6 |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | ping |
| 11 | سناریوی خرابی | مسیر نامتقارن |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | شاهد |
| 14 | معیار پذیرش | ≥ ۴ از ۵ |
| 15 | مستندات نهایی | `03-ops/a6.md` |
| 16 | Cleanup و بازگردانی | — |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="ans-25"></a>

## پاسخ‌های فصل 25

> ابتدا بدون نگاه حل کنید. شناسه: درس-نوع+شماره (ت = تمرین، م = مرور).

**25-1-ت1** — get؟

FGT show.

**25-1-ت2** — ACL؟

Policy.

**25-1-م1** — چرا جدول؟

سرعت.

**25-1-م2** — سناریو: show در FGT؛ چه؟

get.

**25-2-ت1** — Exstart؟

اغلب MTU.

**25-2-ت2** — Timer؟

باید یکی.

**25-2-م1** — چرا MTU؟

Mismatch DBD.

**25-2-م2** — سناریو: Exstart؛ علت؟

MTU.

**25-3-ت1** — Interop؟

هماهنگی.

**25-3-ت2** — Debug؟

هر دو سو.

**25-3-م1** — چرا هر دو سو؟

علت آشکار.

**25-3-م2** — سناریو: یک‌طرفه؛ علت؟

Selector.

**25-4-ت1** — A6؟

FGT+CSR.

**25-4-ت2** — Backup؟

هر دو.

**25-4-م1** — چرا RCA؟

یادگیری.

**25-4-م2** — سناریو: Route نیست؛ علت؟

Redistribute.


---

<a id="ch26"></a>


### پاسخ‌های درس افزوده‌ی 25-0 (فصل 25)

**25-0-ت1** — get router info routing-table all.

**25-0-ت2** — اغلب MTU Mismatch بین دو سر.

**25-0-ت3** — IKEv2، AES-256-GCM، SHA-256، DH 20 (یا ≥ 14)، PFS روشن با همان Group، Lifetime یکسان، DPD، MTU/MSS مشترک، Authentication PSK/Cert.

**25-0-Q1** — Because defaults differ between vendors and cause subtle mismatches.

# فصل 26 — FortiManager و FortiAnalyzer (معماری ۹) و جایگزین‌های بدون لایسنس

**مدت:** ۳۶ ساعت | **پیش‌نیاز:** فصل ۲۲، ۲۵.
**هشدار لایسنس:** FortiManager (FMG) و FortiAnalyzer (FAZ) VM به لایسنس/Evaluation نیاز دارند (`Needs-License`). این فصل **مفهوم و طراحی** را آموزش می‌دهد و **جایگزین عملی بدون لایسنس** (rsyslog/Zabbix و Backup خودکار) را در Lab اجرا می‌کند. هیچ ادعای اجرا روی FMG/FAZ نشده است.
**اهداف:** مدیریت مرکزی؛ Policy Package؛ Log مرکزی؛ جایگزین.
**اشتباهات رایج:** انتظار FMG/FAZ رایگان؛ نبود Backup.

**درس‌های فصل:**
- [درس 26-1 — مفهوم FMG/FAZ و لایسنس](#l-26-1)
- [درس 26-2 — Syslog مرکزی (جایگزین FAZ)](#l-26-2)
- [درس 26-3 — Backup خودکار و Config Management](#l-26-3)
- [درس 26-4 — طراحی معماری ۹ و آزمون](#l-26-4)

---

<a id="l-26-1"></a>

## درس 26-0 — مدیریت مرکزی: معماری FortiManager و FortiAnalyzer، ADOM، Policy Package و محدودیت لایسنس

**فصل ۲۶ · درس افزوده (پیش‌درس ۲۶-۱) · پیش‌نیاز: ۱۲-۰، ۱۳-۷، ۲۲-۰ · ≈ ۵ ساعت**

> **وضعیت (FortiManager/FortiAnalyzer 7.0):** مفهوم ADOM، Install Wizard، افزودن FAZ و تداخل Log Forwarding از مستند رسمی بررسی شد ([Device Manager](https://docs.fortinet.com/document/fortimanager/7.0.0/administration-guide/478145/device-manager)، [Add FortiAnalyzer](https://docs.fortinet.com/document/fortimanager/7.0.0/administration-guide/654379/add-fortianalyzer)، [Installing policy packages](https://docs.fortinet.com/document/fortimanager/7.0.7/administration-guide/153046/installing-policy-packages-and-device-settings)). **Needs-License:** FMG/FAZ VM به لایسنس/Evaluation نیاز دارند؛ **هیچ ادعای اجرا روی آن‌ها نشده است.** جزئیات لایسنس VM باید از مستند/فروشنده تأیید شود (`Unverified`). Lab: جایگزین عملی با rsyslog و Backup.

### ۱) هدف آموزشی

1. نقش **FMG** (مدیریت پیکربندی) و **FAZ** (Log/Report) را تفکیک کند.
2. **ADOM، Device Manager، Policy Package، Install** و **Revision** را توضیح دهد.
3. معماری مدیریت مرکزی برای ۱۰ تا ۱۰۰ دستگاه را طراحی و ریسک‌ها را بگوید.
4. **جایگزین بدون لایسنس** (Syslog مرکزی + Git/Backup + Ansible/API) را طراحی کند.
5. RBAC و Audit مدیریت مرکزی را بنویسد.

### ۲) مفهوم پایه

مدیریت ۲۰ فایروال یکی‌یکی = ناهمگونی، خطا، بی‌Audit. **FMG** پیکربندی/Policy را مرکزی نگه می‌دارد و به دستگاه‌ها «نصب» می‌کند؛ **FAZ** Logها را جمع و تحلیل می‌کند. مرکزی‌سازی هم **سطح حمله** و هم **نقطه‌ی شکست** جدید است.

### ۳) توضیح عمیق فنی

#### ۳-۱) اجزا

- **Device Manager:** ثبت دستگاه‌ها و گروه‌ها، وضعیت Sync.
- **ADOM (Administrative Domain):** بخش مجزا برای دستگاه‌ها/مدیران؛ هر ADOM Policy Package و Object خودش را دارد (برای Multi-tenant یا نسخه‌های مختلف).
- **Policy Package:** مجموعه‌ی Policy/Object که به یک یا چند دستگاه **نصب (Install)** می‌شود؛ مستند: Install Wizard → انتخاب Package و مقصد و زمان‌بندی اختیاری.
- **Device Settings:** تنظیمات مختص دستگاه (Interface، Route).
- **Revision History:** نسخه‌ی تنظیمات؛ بازگشت (Revert).

#### ۳-۲) FAZ

- FAZ Logهای FortiGate را جمع می‌کند (Log Forwarding/Fetching).
- طبق مستند: در FMG با ADOM فعال می‌توان یک FAZ به هر ADOM وصل کرد؛ نام ADOM باید در هر دو یکی باشد؛ و **وقتی ویژگی‌های FAZ در FMG فعال است، Log Forwarding/Fetching/Aggregation پشتیبانی نمی‌شود**؛ افزودن FAZ، قابلیت‌های FAZ را خودکار فعال می‌کند و غیرفعال‌شدنی نیست.

#### ۳-۳) ریسک‌های مرکزی‌سازی

| ریسک | کاهش |
|---|---|
| FMG هدف حمله/نقطه‌ی شکست | شبکه‌ی مدیریت جدا، HA، RBAC، MFA |
| Install اشتباه روی همه | Staging/ADOM آزمایشی، Install Preview، Revision |
| Sync نامنظم | بررسی وضعیت Sync، Install زمان‌بندی‌شده |
| لایسنس | برنامه‌ریزی/جایگزین |

#### ۳-۴) جایگزین بدون لایسنس (برای Lab)

``` text
Config backup : execute backup config tftp/sftp (daily) -> Git repo (no secrets)
Logs          : config log syslogd setting -> rsyslog -> (Zabbix/ELK)
Monitoring    : SNMPv3 + Zabbix
Automation    : REST API/Ansible (read-first)
Change record : ticket + diff of configs
```

#### ۳-۵) Syslog (جایگزین FAZ)

طبق CLI Reference 7.0: `config log syslogd setting` گزینه‌های `server`، `port` (پیش‌فرض 514)، `mode` (udp، reliable، legacy-reliable)، `facility`، `source-ip`، `format` (default، csv، cef، rfc5424) و TLS را دارد؛ **حالت reliable** برای Extended Logging لازم است (مستند Log Message Reference).

### ۴) مثال حل‌شده

**نیاز:** Log مرکزی بدون FAZ.

``` text
config log syslogd setting
    set status enable
    set server "192.168.90.20"
    set mode reliable
    set port 514
    set format rfc5424
    set facility local7
end
```

(ممکن است برای TCP/TLS پورت دیگری لازم باشد؛ سینتکس `Unverified`.) سمت rsyslog: Listener TCP، قالب RFC5424، چرخش Log. **آزمون:** تولید رویداد (Login ناموفق) و دیدن آن در سرور؛ بررسی Timestamp و NTP.

**مثال متوسط:** پس از Install Policy Package به ۳ دستگاه، یکی خطا می‌دهد؛ روش: Install Preview، Revision Diff، Rollback، بررسی وابستگی (Interface Mapping).

**مثال سخت (طراحی):** ۴ شعبه + HQ؛ ADOM برای هر واحد؟ تصمیم: ADOM بر اساس نسخه FortiOS یا مستأجر؛ نه صرفاً جغرافیا؛ Policy Package پایه + Override محلی.

### ۵) GUI و CLI

**GUI FMG:** Device Manager → Add Device؛ Policy & Objects → Policy Package → Install. **GUI FGT:** Security Fabric/Central Management. **CLI FGT:**

``` text
config system central-management
    set type fortimanager
    set fmg "192.168.90.30"
end
```

(`Unverified`.)

### ۶) نکات امنیتی

- مدیریت مرکزی فقط از شبکه‌ی مدیریت؛ Admin جدا با MFA.
- Log شامل داده‌ی حساس است؛ رمزنگاری انتقال/ذخیره.
- بدون Audit تغییرات، Change ثبت نمی‌شود.

### ۷) جمع‌بندی

- FMG پیکربندی؛ FAZ Log؛ ADOM جداسازی؛ Policy Package نصب.
- مرکزی‌سازی ریسک جدید ایجاد می‌کند.
- جایگزین بدون لایسنس: Syslog، Git، SNMPv3، API.
- ادعای اجرا بدون دستگاه ممنوع.

### ۸) تمرین و ارزیابی

**ت1.** (ساده) FMG و FAZ چه فرقی دارند؟ *(پاسخ: 26-0-ت1)*

**ت2.** (ساده) ADOM چیست؟ *(پاسخ: 26-0-ت2)*

**ت3.** (متوسط) چرا Install Preview لازم است؟ *(پاسخ: 26-0-ت3)*

**ت4.** (سخت) معماری جایگزین بدون لایسنس را برای ۱۰ فایروال بنویسید. *(پاسخ: 26-0-ت4)*

**Q1.** Quick quiz (English): What is an ADOM used for? *(پاسخ: 26-0-Q1)*

### ۹) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| FMG | FortiManager | مدیریت مرکزی |
| FAZ | FortiAnalyzer | تحلیل Log |
| ADOM | Administrative Domain | دامنه‌ی مدیریتی |
| RBAC | Role-Based Access Control | دسترسی نقش‌محور |

- *Preview before installing a policy package.* ← قبل از نصب Policy Package پیش‌نمایش بگیرید.

### ۱۰) منابع

- Fortinet Docs: [Device Manager](https://docs.fortinet.com/document/fortimanager/7.0.0/administration-guide/478145/device-manager)، [Add FortiAnalyzer](https://docs.fortinet.com/document/fortimanager/7.0.0/administration-guide/654379/add-fortianalyzer)، [Installing policy packages](https://docs.fortinet.com/document/fortimanager/7.0.7/administration-guide/153046/installing-policy-packages-and-device-settings)، [config log syslogd setting](https://docs.fortinet.com/document/fortigate/7.0.0/cli-reference/456620/config-log-syslogd-setting).

## درس 26-1 — مفهوم FMG/FAZ و لایسنس

**فصل 26 - روز 1 · پیش‌نیاز: فصل ۲۵ · ۶ ساعت**

### ۱) معرفی درس

نقش هر یک و محدودیت لایسنس.

### ۲) پیش‌نیازها

فصل ۲۵

### ۳) توضیح مفهومی

- FMG: Policy Package و Device Manager.
- FAZ: Log/Report.
- VM License.
- Evaluation محدود.
- طراحی بدون ابزار.

### ۴) مثال ساده

مدیریت ده فایروال از یک نقطه.

### ۵) مثال سازمانی

سازمان: FMG برای Policy و FAZ برای Log.

### ۶) تصویر و توپولوژی

```text
FGT×N -> FMG/FAZ
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. Security Fabric > Fabric Connectors.

#### روش خط فرمان (CLI)

```text
get system central-management
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- `Unverified`.

### ۸) تست عملکرد

- جدول مقایسه با جایگزین.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | FMG در دسترس نیست |
| شواهد/دستور | — |
| علت | لایسنس |
| رفع | جایگزین |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** FMG؟ *(پاسخ: 26-1-ت1)*

**ت2.** FAZ؟ *(پاسخ: 26-1-ت2)*

### ۱۱) مرور و ارزیابی

**م1.** چرا جایگزین؟ *(پاسخ: 26-1-م1)*

**م2.** سناریو: بدون FAZ؛ Log کجا؟ *(پاسخ: 26-1-م2)*

**معیار تسلط:** مفهوم و جایگزین.

**اشتباهات رایج:** لایسنس.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| FMG | FortiManager | مدیریت مرکزی | Fortinet |
| FAZ | FortiAnalyzer | تحلیل Log | Fortinet |

| English sentence | ترجمه |
|---|---|
| Plan a fallback when licenses are missing. | وقتی لایسنس نیست جایگزین برنامه‌ریزی کنید. |

#### کارت Lab — درس 26-1

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | مقایسه |
| 2 | پیش‌نیاز | فصل ۲۵ |
| 3 | توپولوژی | — |
| 4 | تجهیزات | — |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | — |
| 7 | وضعیت اولیه | — |
| 8 | صورت مسئله | جدول |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | — |
| 11 | سناریوی خرابی | FMG در دسترس نیست |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | سند |
| 14 | معیار پذیرش | تأیید |
| 15 | مستندات نهایی | `02-design/fmg-faz.md` |
| 16 | Cleanup و بازگردانی | — |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="l-26-2"></a>

## درس 26-2 — Syslog مرکزی (جایگزین FAZ)

**فصل 26 - روز 2 · پیش‌نیاز: درس ۲۶-۰ · ۶ ساعت**

### ۱) معرفی درس

ارسال Log به rsyslog.

### ۲) پیش‌نیازها

درس ۲۶-۰

### ۳) توضیح مفهومی

- `config log syslogd setting`.
- rsyslog روی Linux.
- فیلتر.
- Retention.
- تأیید دریافت.

### ۴) مثال ساده

مدیریت ده فایروال از یک نقطه.

### ۵) مثال سازمانی

سازمان: FMG برای Policy و FAZ برای Log.

### ۶) تصویر و توپولوژی

```text
FGT×N -> FMG/FAZ
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. Log & Report > Log Settings > Syslog.

#### روش خط فرمان (CLI)

```text
config log syslogd setting
    set status enable
    set server "192.168.90.20"
    set port 514
end
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- `Unverified`.
- UDP 514.

### ۸) تست عملکرد

- دریافت Log در rsyslog.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | Log نمی‌رسد |
| شواهد/دستور | tcpdump |
| علت | Port/Firewall |
| رفع | اصلاح |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** Syslog؟ *(پاسخ: 26-2-ت1)*

**ت2.** Port؟ *(پاسخ: 26-2-ت2)*

### ۱۱) مرور و ارزیابی

**م1.** چرا مرکزی؟ *(پاسخ: 26-2-م1)*

**م2.** سناریو: Log ناقص؛ علت؟ *(پاسخ: 26-2-م2)*

**معیار تسلط:** مفهوم و جایگزین.

**اشتباهات رایج:** لایسنس.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| Syslog | Syslog | پروتکل Log | Linux |

| English sentence | ترجمه |
|---|---|
| Centralize logs for analysis. | برای تحلیل Log را مرکزی کنید. |

#### کارت Lab — درس 26-2

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | Syslog |
| 2 | پیش‌نیاز | درس ۲۶-۰ |
| 3 | توپولوژی | FGT+Linux |
| 4 | تجهیزات | FGT+Linux |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | 192.168.90.20 |
| 7 | وضعیت اولیه | Baseline |
| 8 | صورت مسئله | Syslog |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | tail |
| 11 | سناریوی خرابی | Log نمی‌رسد |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | Log رسید |
| 14 | معیار پذیرش | ثبت |
| 15 | مستندات نهایی | `03-ops/syslog.md` |
| 16 | Cleanup و بازگردانی | حذف |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="l-26-3"></a>

## درس 26-3 — Backup خودکار و Config Management

**فصل 26 - روز 3 · پیش‌نیاز: درس ۲۶-۱ · ۶ ساعت**

### ۱) معرفی درس

جایگزین FMG: Backup/Git.

### ۲) پیش‌نیازها

درس ۲۶-۱

### ۳) توضیح مفهومی

- Backup دوره‌ای (TFTP/SCP).
- Git برای Config.
- مقایسه Diff.
- Rotation.
- بدون Secret در Git.

### ۴) مثال ساده

مدیریت ده فایروال از یک نقطه.

### ۵) مثال سازمانی

سازمان: FMG برای Policy و FAZ برای Log.

### ۶) تصویر و توپولوژی

```text
FGT×N -> FMG/FAZ
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. System > Config > Backup.

#### روش خط فرمان (CLI)

```text
execute backup config tftp fgt-daily.conf 192.168.90.10
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- `Unverified`.
- Secretها را پاک کنید.

### ۸) تست عملکرد

- Backup شبانه.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | Backup ناقص |
| شواهد/دستور | فایل |
| علت | Permission |
| رفع | اصلاح |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** Diff؟ *(پاسخ: 26-3-ت1)*

**ت2.** Secret؟ *(پاسخ: 26-3-ت2)*

### ۱۱) مرور و ارزیابی

**م1.** چرا Git؟ *(پاسخ: 26-3-م1)*

**م2.** سناریو: رمز در Git؛ چه؟ *(پاسخ: 26-3-م2)*

**معیار تسلط:** مفهوم و جایگزین.

**اشتباهات رایج:** لایسنس.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| Diff | Diff | تفاوت | Ops |

| English sentence | ترجمه |
|---|---|
| Never commit secrets. | هرگز Secret را Commit نکنید. |

#### کارت Lab — درس 26-3

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | Backup |
| 2 | پیش‌نیاز | درس ۲۶-۱ |
| 3 | توپولوژی | FGT+Linux |
| 4 | تجهیزات | FGT+Linux |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | — |
| 7 | وضعیت اولیه | Baseline |
| 8 | صورت مسئله | Backup |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | diff |
| 11 | سناریوی خرابی | Backup ناقص |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | تفاوت |
| 14 | معیار پذیرش | ثبت |
| 15 | مستندات نهایی | `03-ops/backup.md` |
| 16 | Cleanup و بازگردانی | — |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="l-26-4"></a>

## درس 26-4 — طراحی معماری ۹ و آزمون

**فصل 26 - روز 4 · پیش‌نیاز: درس ۲۶-۲ · ۶ ساعت**

### ۱) معرفی درس

طراحی مدیریت مرکزی.

### ۲) پیش‌نیازها

درس ۲۶-۲

### ۳) توضیح مفهومی

- طراحی FMG/FAZ.
- جایگزین.
- RBAC.
- Audit.
- آزمون.

### ۴) مثال ساده

مدیریت ده فایروال از یک نقطه.

### ۵) مثال سازمانی

سازمان: FMG برای Policy و FAZ برای Log.

### ۶) تصویر و توپولوژی

```text
FGT×N -> FMG/FAZ
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. System > Administrators.

#### روش خط فرمان (CLI)

```text
get system admin
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- خواندنی.

### ۸) تست عملکرد

- طرح A9.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | دسترسی زیاد |
| شواهد/دستور | admin list |
| علت | Profile |
| رفع | محدود |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** RBAC؟ *(پاسخ: 26-4-ت1)*

**ت2.** Audit؟ *(پاسخ: 26-4-ت2)*

### ۱۱) مرور و ارزیابی

**م1.** چرا RBAC؟ *(پاسخ: 26-4-م1)*

**م2.** سناریو: همه Admin؛ چه؟ *(پاسخ: 26-4-م2)*

**معیار تسلط:** مفهوم و جایگزین.

**اشتباهات رایج:** لایسنس.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| RBAC | Role-Based Access Control | دسترسی نقش‌محور | امنیت |

| English sentence | ترجمه |
|---|---|
| Use role-based access. | از دسترسی نقش‌محور استفاده کنید. |

#### کارت Lab — درس 26-4

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | آزمون A9 |
| 2 | پیش‌نیاز | درس ۲۶-۲ |
| 3 | توپولوژی | — |
| 4 | تجهیزات | — |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | — |
| 7 | وضعیت اولیه | — |
| 8 | صورت مسئله | طراحی |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | — |
| 11 | سناریوی خرابی | دسترسی زیاد |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | سند |
| 14 | معیار پذیرش | ≥ ۴ از ۵ |
| 15 | مستندات نهایی | `02-design/a9.md` |
| 16 | Cleanup و بازگردانی | — |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="ans-26"></a>

## پاسخ‌های فصل 26

> ابتدا بدون نگاه حل کنید. شناسه: درس-نوع+شماره (ت = تمرین، م = مرور).

**26-1-ت1** — FMG؟

مدیریت مرکزی.

**26-1-ت2** — FAZ؟

Log.

**26-1-م1** — چرا جایگزین؟

لایسنس.

**26-1-م2** — سناریو: بدون FAZ؛ Log کجا؟

rsyslog.

**26-2-ت1** — Syslog؟

ارسال Log.

**26-2-ت2** — Port؟

514.

**26-2-م1** — چرا مرکزی؟

تحلیل.

**26-2-م2** — سناریو: Log ناقص؛ علت؟

UDP loss.

**26-3-ت1** — Diff؟

تفاوت Config.

**26-3-ت2** — Secret؟

حذف.

**26-3-م1** — چرا Git؟

تاریخچه.

**26-3-م2** — سناریو: رمز در Git؛ چه؟

حذف و چرخش.

**26-4-ت1** — RBAC؟

نقش.

**26-4-ت2** — Audit؟

ثبت.

**26-4-م1** — چرا RBAC؟

حداقل دسترسی.

**26-4-م2** — سناریو: همه Admin؛ چه؟

Profile.


---

<a id="ch27"></a>


### پاسخ‌های درس افزوده‌ی 26-0 (فصل 26)

**26-0-ت1** — FMG پیکربندی/Policy مرکزی؛ FAZ جمع‌آوری و تحلیل Log.

**26-0-ت2** — دامنه‌ی مدیریتی مجزا برای دستگاه‌ها/مدیران با Policy Package و Object خودش.

**26-0-ت3** — تا تأثیر نصب پیش از اعمال دیده شود و خطای گسترده رخ ندهد.

**26-0-ت4** — Syslog مرکزی (rsyslog)، Backup روزانه به Git/SFTP بدون Secret، SNMPv3 + Zabbix، Ansible/API خواندنی، ثبت Change با Diff.

**26-0-Q1** — To separate devices, administrators and policy sets into administrative domains (for example per tenant or version).

# فصل 27 — Logging، Monitoring، Performance، API، Hardening و Backup (G10)

**مدت:** ۳۶ ساعت | **پیش‌نیاز:** فصل ۱۴، ۲۶.
**اهداف:** Logging؛ SNMP و Zabbix؛ Performance Baseline؛ REST API؛ Hardening؛ Backup/Restore. Gate G10: مانیتورینگ+Log+Hardening+Backup با شاهد.
**اشتباهات رایج:** SNMP v2c باز؛ API Token بی‌محدودیت؛ Admin روی WAN؛ Backup بدون تست Restore.

**درس‌های فصل:**
- [درس 27-1 — Logging و Log Settings](#l-27-1)
- [درس 27-2 — SNMP و مانیتورینگ Zabbix](#l-27-2)
- [درس 27-3 — REST API و Automation](#l-27-3)
- [درس 27-4 — Hardening و Backup/Restore](#l-27-4)
- [درس 27-5 — Gate G10 و آزمون](#l-27-5)

---

<a id="l-27-1"></a>

## درس 27-0 — Logging، Monitoring و Baseline: چه چیزی را، چرا و چگونه ثبت و پایش کنیم

**فصل ۲۷ · درس افزوده (پیش‌درس ۲۷-۱) · پیش‌نیاز: ۱۴-۷، ۲۶-۰ · ≈ ۶ ساعت**

> **وضعیت (FortiOS 7.0):** انواع Log و گزینه‌های Syslog از مستند رسمی ([Sample logs by log type](https://docs.fortinet.com/document/fortigate/7.0.5/administration-guide/986892/sample-logs-by-log-type)، [syslogd setting](https://docs.fortinet.com/document/fortigate/7.0.0/cli-reference/456620/config-log-syslogd-setting)) تأیید شد. SNMPv3 و REST API روی FortiGate در این دور تأیید نشد و `Unverified` است.

### ۱) هدف آموزشی

1. انواع Log (Traffic، Event، UTM) و **سطح ثبت** را بشناسد و بر اساس هدف انتخاب کند.
2. **Baseline** عملکرد (CPU، Memory، Session، Throughput) بسازد و انحراف را تشخیص دهد.
3. معیارهای مانیتورینگ و **آستانه‌ی هشدار** معنادار تعیین کند (نه فقط «روشن/خاموش»).
4. Log را با NTP همگام و در مقصد مرکزی نگه دارد (Retention).
5. از Log به **تحلیل حادثه** برسد.

### ۲) مفهوم پایه

Log بدون هدف = انبار داده؛ Monitoring بدون Baseline = «همه چیز نرمال است» یا «همه چیز بد است» بدون مرجع. سه سؤال: **چه چیزی ثبت شود؟ برای چه تصمیمی؟ چه کسی می‌بیند و چه زمانی؟**

### ۳) توضیح عمیق فنی

#### ۳-۱) انواع Log

| نوع | محتوا | کاربرد |
|---|---|---|
| Traffic (Forward/Local) | Sessionها: Source/Dest/Service/Action/Policy | تحلیل جریان، حادثه |
| Event | Login مدیر، تغییر Config، VPN، HA، System | Audit، تغییر |
| UTM/Security | AV، Web، DNS، App، IPS، DLP | تهدید |

طبق مستند: Log امنیتی نیاز دارد که Policy دارای UTM باشد و `logtraffic` روی `utm` یا `all`. **Policyهای Deny** را هم Log کنید؛ Policy 0 (Implicit deny) با تنظیم جدا قابل Log است (`Unverified`).

#### ۳-۲) سطح Log و هزینه

`logtraffic all` همه‌ی Session‌ها (حجم زیاد)؛ `utm` فقط Sessionهای دارای رویداد UTM. تصمیم: Allow مهم و همه‌ی Deny؛ سرویس‌های پرحجم بی‌اهمیت: خاموش. **حجم Log = Session × اندازه‌ی رکورد.**

#### ۳-۳) Baseline

قبل از مشکل، در یک هفته‌ی عادی اندازه بگیرید و نگه دارید: CPU/Memory میانگین و پیک، تعداد Session، Throughput، Interface Errors، تعداد VPN، حجم Log. «CPU 70٪» بدون Baseline معنی ندارد: برای یک دستگاه عادی و برای دیگری اوج حمله.

#### ۳-۴) آستانه‌ها (نمونه؛ برای محیط خود تنظیم کنید)

| معیار | هشدار | بحرانی | دلیل |
|---|---|---|---|
| CPU | > 70٪ ۵ دقیقه | > 90٪ | ظرفیت |
| Memory | > 80٪ | > 90٪ (Conserve mode) | ظرفیت |
| Session | > 70٪ حد | > 90٪ | Exhaustion |
| Interface Error | رشد مداوم | — | کابل/Duplex |
| HA | عضو Out-of-sync | Failover | دسترس‌پذیری |
| VPN | Tunnel Down | — | وصل نبودن |
| Disk Log | > 80٪ | > 90٪ | از دست رفتن Log |

#### ۳-۵) ابزارها

- **Syslog:** ارسال Log به سرور مرکزی (UDP/TCP/TLS؛ `format rfc5424`/`cef`)؛ حالت reliable ضروری برای Extended Logging.
- **SNMP** (ترجیحاً v3): پایش Interface/CPU/Memory با Zabbix.
- **API/CLI:** جمع‌آوری وضعیت (`get system performance status`، `diagnose sys top`).
- **NTP:** بدون زمان یکسان Log چند دستگاه قابل Correlation نیست.

#### ۳-۶) از Log به حادثه

مثال تحلیل: «Deny زیاد از 198.51.100.7 به پورت‌های متعدد» ← Port Scan. Correlation: همان IP در Log DNS/Web؟ آیا موفق شد؟ اقدام: Block، بازبینی. این پایه‌ی فصل ۲۹ است.

### ۴) مثال حل‌شده

``` text
config firewall policy
    edit 10
        set logtraffic all
    next
end
config log syslogd setting
    set status enable
    set server "192.168.90.20"
    set mode reliable
    set format rfc5424
end
get system performance status
diagnose sys top 2 20
```

(`Unverified`.) **برنامه‌ی Baseline:** هر ۵ دقیقه ۷ روز؛ جدول میانگین/پیک؛ آستانه‌ها = Baseline × ضریب.

**مثال متوسط:** CPU ناگهان 85٪: تقسیم مسیر: Session جدید (حمله؟)، Profile/UTM، Local-in (Scan مدیریتی)، Log. شواهد: `sys top`، `session statistics`، Log Deny.

**مثال سخت:** Log دیسک پر و Log حادثه از دست رفت: راه‌حل: Syslog مرکزی reliable + Retention + هشدار Disk.

### ۵) GUI و CLI

**GUI:** Log & Report → Log Settings؛ Forward Traffic؛ Events؛ Dashboard → Performance؛ FortiView. **CLI:** `get log ...`، `get system performance status`.

### ۶) نکات امنیتی

- Log حاوی IP/User است؛ دسترسی محدود و رمزنگاری انتقال.
- از Log پاک نکردن برای مخفی‌کردن؛ Immutable storage.
- Timestamp دقیق (NTP) برای ارزش قانونی.

### ۷) جمع‌بندی

- ثبت هدفمند؛ Baseline قبل از مشکل؛ آستانه‌ی مبتنی بر Baseline.
- Log مرکزی reliable، NTP هماهنگ.
- Log→Correlation→حادثه.

### ۸) تمرین و ارزیابی

**ت1.** (ساده) سه نوع Log را بگویید. *(پاسخ: 27-0-ت1)*

**ت2.** (متوسط) چرا Baseline لازم است؟ *(پاسخ: 27-0-ت2)*

**ت3.** (سخت) آستانه‌های هشدار برای ۶ معیار با دلیل بنویسید. *(پاسخ: 27-0-ت3)*

**ت4.** (سخت، طراحی) برنامه‌ی Retention برای ۱۸۰ روز Log با حجم ۲ GB/روز. *(پاسخ: 27-0-ت4)*

**Q1.** Quick quiz (English): Why must firewall clocks be synchronized with NTP? *(پاسخ: 27-0-Q1)*

### ۹) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Baseline | Performance baseline | مرجع وضعیت عادی |
| SNMP | Simple Network Management Protocol | پروتکل پایش |
| Retention | Log retention | مدت نگهداری |
| Correlation | Log correlation | همبستگی Log |

- *Establish a baseline before setting alert thresholds.* ← قبل از آستانه‌ها Baseline بسازید.

### ۱۰) منابع

- Fortinet Docs: [Sample logs by log type](https://docs.fortinet.com/document/fortigate/7.0.5/administration-guide/986892/sample-logs-by-log-type)، [config log syslogd setting](https://docs.fortinet.com/document/fortigate/7.0.0/cli-reference/456620/config-log-syslogd-setting)؛ NIST SP 800-92 — Guide to Log Management.

## درس 27-1 — Logging و Log Settings

**فصل 27 - روز 1 · پیش‌نیاز: فصل ۲۶ · ۶ ساعت**

### ۱) معرفی درس

چه چیزی Log شود و کجا.

### ۲) پیش‌نیازها

فصل ۲۶

### ۳) توضیح مفهومی

- Traffic/Event/UTM Log.
- Disk/Memory.
- Syslog.
- Retention.
- Privacy.

### ۴) مثال ساده

کنترل سلامت فایروال.

### ۵) مثال سازمانی

سازمان: مانیتورینگ و Hardening استاندارد.

### ۶) تصویر و توپولوژی

```text
FGT -> SNMP/Syslog -> Zabbix
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. Log & Report > Log Settings.

#### روش خط فرمان (CLI)

```text
config log setting
    set local-in-allow enable
end
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- `Unverified`.

### ۸) تست عملکرد

- تنظیم Log.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | Disk پر |
| شواهد/دستور | get log |
| علت | Retention |
| رفع | تنظیم |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** Traffic Log؟ *(پاسخ: 27-1-ت1)*

**ت2.** Retention؟ *(پاسخ: 27-1-ت2)*

### ۱۱) مرور و ارزیابی

**م1.** چرا Retention؟ *(پاسخ: 27-1-م1)*

**م2.** سناریو: Log قدیمی نیست؛ علت؟ *(پاسخ: 27-1-م2)*

**معیار تسلط:** Monitoring و Hardening.

**اشتباهات رایج:** پیش‌فرض ناامن.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| Log | Log | ثبت | FGT |

| English sentence | ترجمه |
|---|---|
| Set a log retention policy. | سیاست نگهداری Log تعیین کنید. |

#### کارت Lab — درس 27-1

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | Log |
| 2 | پیش‌نیاز | فصل ۲۶ |
| 3 | توپولوژی | FGT |
| 4 | تجهیزات | FGT |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | — |
| 7 | وضعیت اولیه | Baseline |
| 8 | صورت مسئله | Log |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | — |
| 11 | سناریوی خرابی | Disk پر |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | تنظیم |
| 14 | معیار پذیرش | ثبت |
| 15 | مستندات نهایی | `03-ops/log.md` |
| 16 | Cleanup و بازگردانی | — |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="l-27-2"></a>

## درس 27-2 — SNMP و مانیتورینگ Zabbix

**فصل 27 - روز 2 · پیش‌نیاز: درس ۲۷-۰ · ۶ ساعت**

### ۱) معرفی درس

پایش CPU/Memory/Interface.

### ۲) پیش‌نیازها

درس ۲۷-۰

### ۳) توضیح مفهومی

- SNMPv3 ترجیح.
- Community v2c فقط Lab.
- Zabbix Template.
- Trigger.
- Dashboard.

### ۴) مثال ساده

کنترل سلامت فایروال.

### ۵) مثال سازمانی

سازمان: مانیتورینگ و Hardening استاندارد.

### ۶) تصویر و توپولوژی

```text
FGT -> SNMP/Syslog -> Zabbix
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. System > SNMP.

#### روش خط فرمان (CLI)

```text
config system snmp sysinfo
    set status enable
end
config system snmp user
    edit "mon"
        set security-level auth-priv
    next
end
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- `Unverified`.
- v2c ناامن.

### ۸) تست عملکرد

- Zabbix Host.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | SNMP timeout |
| شواهد/دستور | snmpwalk |
| علت | ACL |
| رفع | allowaccess |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** SNMPv3؟ *(پاسخ: 27-2-ت1)*

**ت2.** Template؟ *(پاسخ: 27-2-ت2)*

### ۱۱) مرور و ارزیابی

**م1.** چرا v3؟ *(پاسخ: 27-2-م1)*

**م2.** سناریو: v2c باز؛ چه؟ *(پاسخ: 27-2-م2)*

**معیار تسلط:** Monitoring و Hardening.

**اشتباهات رایج:** پیش‌فرض ناامن.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| SNMP | Simple Network Management Protocol | مانیتورینگ | Ops |

| English sentence | ترجمه |
|---|---|
| Prefer SNMPv3. | SNMPv3 را ترجیح دهید. |

#### کارت Lab — درس 27-2

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | SNMP |
| 2 | پیش‌نیاز | درس ۲۷-۰ |
| 3 | توپولوژی | FGT+Zabbix |
| 4 | تجهیزات | FGT+Zabbix |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | — |
| 7 | وضعیت اولیه | Baseline |
| 8 | صورت مسئله | SNMP |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | snmpwalk |
| 11 | سناریوی خرابی | SNMP timeout |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | داده |
| 14 | معیار پذیرش | ثبت |
| 15 | مستندات نهایی | `03-ops/snmp.md` |
| 16 | Cleanup و بازگردانی | حذف |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="l-27-3"></a>

## درس 27-3 — REST API و Automation

**فصل 27 - روز 3 · پیش‌نیاز: درس ۲۷-۱ · ۶ ساعت**

### ۱) معرفی درس

خودکارسازی با API Token.

### ۲) پیش‌نیازها

درس ۲۷-۱

### ۳) توضیح مفهومی

- API Admin با Token.
- Trusthost.
- GET وضعیت.
- Postman/curl.
- Token را ذخیره نکنید.

### ۴) مثال ساده

کنترل سلامت فایروال.

### ۵) مثال سازمانی

سازمان: مانیتورینگ و Hardening استاندارد.

### ۶) تصویر و توپولوژی

```text
FGT -> SNMP/Syslog -> Zabbix
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. System > Administrators > REST API Admin.

#### روش خط فرمان (CLI)

```text
curl -k -H "Authorization: Bearer <API-TOKEN>" https://192.168.90.1/api/v2/monitor/system/status
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- Token نمونه؛ `Unverified`.

### ۸) تست عملکرد

- GET وضعیت.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | 401 |
| شواهد/دستور | curl |
| علت | Token/Trusthost |
| رفع | اصلاح |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** Token؟ *(پاسخ: 27-3-ت1)*

**ت2.** Trusthost؟ *(پاسخ: 27-3-ت2)*

### ۱۱) مرور و ارزیابی

**م1.** چرا Trusthost؟ *(پاسخ: 27-3-م1)*

**م2.** سناریو: 401؛ علت؟ *(پاسخ: 27-3-م2)*

**معیار تسلط:** Monitoring و Hardening.

**اشتباهات رایج:** پیش‌فرض ناامن.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| API | Application Programming Interface | رابط برنامه‌نویسی | Automation |

| English sentence | ترجمه |
|---|---|
| Restrict API tokens by trusted host. | Token API را با Trusthost محدود کنید. |

#### کارت Lab — درس 27-3

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | API |
| 2 | پیش‌نیاز | درس ۲۷-۱ |
| 3 | توپولوژی | FGT+Linux |
| 4 | تجهیزات | FGT+Linux |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | — |
| 7 | وضعیت اولیه | Baseline |
| 8 | صورت مسئله | API |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | curl |
| 11 | سناریوی خرابی | 401 |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | JSON |
| 14 | معیار پذیرش | ثبت |
| 15 | مستندات نهایی | `03-ops/api.md` |
| 16 | Cleanup و بازگردانی | حذف |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="l-27-4"></a>

## درس 27-4 — Hardening و Backup/Restore

**فصل 27 - روز 4 · پیش‌نیاز: درس ۲۷-۲ · ۶ ساعت**

### ۱) معرفی درس

تنظیمات ایمن و بازیابی.

### ۲) پیش‌نیازها

درس ۲۷-۲

### ۳) توضیح مفهومی

- Admin فقط Mgmt.
- Timeout، Lockout.
- غیرفعال HTTP/Telnet.
- Backup و تست Restore.
- Patch.

### ۴) مثال ساده

کنترل سلامت فایروال.

### ۵) مثال سازمانی

سازمان: مانیتورینگ و Hardening استاندارد.

### ۶) تصویر و توپولوژی

```text
FGT -> SNMP/Syslog -> Zabbix
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. System > Settings.

#### روش خط فرمان (CLI)

```text
config system global
    set admintimeout 10
    set admin-https-redirect enable
end
execute backup config tftp fgt-g10.conf 192.168.90.10
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- `Unverified`.

### ۸) تست عملکرد

- Backup و Restore آزمایشی.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | Restore شکست |
| شواهد/دستور | execute restore |
| علت | نسخه |
| رفع | تطبیق |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** Hardening؟ *(پاسخ: 27-4-ت1)*

**ت2.** Restore؟ *(پاسخ: 27-4-ت2)*

### ۱۱) مرور و ارزیابی

**م1.** چرا تست Restore؟ *(پاسخ: 27-4-م1)*

**م2.** سناریو: Telnet باز؛ چه؟ *(پاسخ: 27-4-م2)*

**معیار تسلط:** Monitoring و Hardening.

**اشتباهات رایج:** پیش‌فرض ناامن.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| Hardening | Hardening | ایمن‌سازی | امنیت |

| English sentence | ترجمه |
|---|---|
| Test your restores. | Restore را تست کنید. |

#### کارت Lab — درس 27-4

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | Hardening |
| 2 | پیش‌نیاز | درس ۲۷-۲ |
| 3 | توپولوژی | FGT |
| 4 | تجهیزات | FGT |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | — |
| 7 | وضعیت اولیه | Baseline |
| 8 | صورت مسئله | Hardening |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | — |
| 11 | سناریوی خرابی | Restore شکست |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | چک‌لیست |
| 14 | معیار پذیرش | ثبت |
| 15 | مستندات نهایی | `03-ops/hardening.md` |
| 16 | Cleanup و بازگردانی | — |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="l-27-5"></a>

## درس 27-5 — Gate G10 و آزمون

**فصل 27 - روز 5 · پیش‌نیاز: درس ۲۷-۳ · ۶ ساعت**

### ۱) معرفی درس

ارزیابی.

### ۲) پیش‌نیازها

درس ۲۷-۳

### ۳) توضیح مفهومی

- مانیتورینگ.
- Log.
- Hardening.
- Backup.
- آزمون.

### ۴) مثال ساده

کنترل سلامت فایروال.

### ۵) مثال سازمانی

سازمان: مانیتورینگ و Hardening استاندارد.

### ۶) تصویر و توپولوژی

```text
FGT -> SNMP/Syslog -> Zabbix
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. Dashboard.

#### روش خط فرمان (CLI)

```text
get system status
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- خواندنی.

### ۸) تست عملکرد

- اجرای G10.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | G10 ناقص |
| شواهد/دستور | چک‌لیست |
| علت | مورد جاافتاده |
| رفع | تکمیل |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** G10؟ *(پاسخ: 27-5-ت1)*

**ت2.** شاهد؟ *(پاسخ: 27-5-ت2)*

### ۱۱) مرور و ارزیابی

**م1.** چرا شاهد؟ *(پاسخ: 27-5-م1)*

**م2.** سناریو: بدون Backup؛ G10؟ *(پاسخ: 27-5-م2)*

**معیار تسلط:** Monitoring و Hardening.

**اشتباهات رایج:** پیش‌فرض ناامن.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| G10 | Gate 10 | دروازه‌ی ۱۰ | دوره |

| English sentence | ترجمه |
|---|---|
| Collect evidence for every gate. | برای هر Gate شاهد جمع کنید. |

#### کارت Lab — درس 27-5

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | آزمون G10 |
| 2 | پیش‌نیاز | درس ۲۷-۳ |
| 3 | توپولوژی | FGT |
| 4 | تجهیزات | FGT |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | — |
| 7 | وضعیت اولیه | Baseline |
| 8 | صورت مسئله | G10 |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | تست |
| 11 | سناریوی خرابی | G10 ناقص |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | شاهد |
| 14 | معیار پذیرش | ≥ ۴ از ۵ |
| 15 | مستندات نهایی | `03-ops/g10.md` |
| 16 | Cleanup و بازگردانی | — |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="ans-27"></a>

## درس 27-7 — Hardening، Backup/Restore و API: امن‌سازی مدیریتی و بازیابی قابل‌اثبات

**فصل ۲۷ · درس افزوده (پس از ۲۷-۵) · پیش‌نیاز: ۱۲-۸، ۲۶-۰، ۲۷-۰ · ≈ ۶ ساعت**

> **وضعیت (FortiOS 7.0.3):** اصول از دانش عملیاتی و Local-in (۱۲-۸)؛ دستورهای `Unverified`؛ **REST API و SNMPv3 در این دور با مستند رسمی تأیید نشد** (به مرجع 7.0 مراجعه شود). Lab «اجرا نشده».

### ۱) هدف آموزشی

1. چک‌لیست Hardening مدیریتی (Admin، Access، سرویس‌ها، زمان‌بندی) را اجرا و دلیل هر مورد را بگوید.
2. **Backup/Restore** را طوری انجام دهد که «بازیابی‌شدنی بودن» اثبات شود.
3. **API/Automation** را با Least Privilege و Trusted Host محدود و ایمن به‌کار بگیرد.
4. تغییرات مدیریتی را Audit و Rollback کند.

### ۲) مفهوم پایه

فایروال لبه با پیش‌فرض‌های «راحت» ایمن نیست. Hardening یعنی کاهش سطح حمله: هر سرویس/حساب/پورت غیرضروری را ببندید و هر چه باقی ماند محافظت و پایش شود. Backup بدون **تست Restore** ادعاست، نه تضمین.

### ۳) توضیح عمیق فنی

#### ۳-۱) چک‌لیست Hardening

| حوزه | اقدام | دلیل |
|---|---|---|
| Admin | تغییر رمز/نام admin پیش‌فرض، حساب شخصی، حذف حساب مشترک | Accountability |
| دسترسی | `allowaccess` حداقل، Trusted Host، Local-in Policy | سطح حمله (۱۲-۸) |
| پروتکل | غیرفعال Telnet/HTTP؛ HTTPS/SSH با TLS/Cipher مناسب | رمزنگاری |
| MFA | برای Admin | سرقت رمز |
| Timeout/Lockout | `admintimeout`، `admin-lockout-*` | Brute-force |
| Profile | Admin Profile حداقلی (Read-only برای Audit) | Least Privilege |
| زمان | NTP امن | Log معتبر |
| Banner/Log | Log تغییر Config و Login | Audit |
| Patch | پیگیری PSIRT؛ نسخه‌ی 7.0.3 قدیمی است | CVE |

#### ۳-۲) Backup

- **چه چیزی:** Config (کامل)، Certificate/Key (جدا و رمزشده)، لیست نسخه/Serial/لایسنس.
- **کجا:** مقصد خارج از دستگاه (SFTP/Git)، رمزنگاری، Retention (روزانه/هفتگی).
- **امنیت:** فایل Config شامل Hash/رمز رمزگذاری‌شده است ولی حساس؛ هرگز در مخزن عمومی؛ پاک‌کردن Secret قبل از Git.
- **تست Restore:** در Lab با همان نسخه و Interface؛ بازیابی و مقایسه `show` پیکربندی؛ ثبت زمان RTO.

#### ۳-۳) API و Automation

اصول: حساب/Token **فقط** با Profile لازم؛ **Trusted Host** (IP مبدأ)؛ Token در Vault/متغیر محیطی؛ شروع با GET (خواندنی)؛ هر POST/PUT با Change؛ Log تماس‌های API. `Unverified`: روش ایجاد Token و مسیرهای `/api/v2/...` در 7.0.3 را با مرجع تأیید کنید.

#### ۳-۴) Audit و Rollback

- هر تغییر: Ticket، Diff Config، تأییدکننده.
- Rollback: Config قبلی + Session (۱۳-۷) + تست مثبت/منفی.
- «تغییر اضطراری» هم ثبت شود.

### ۴) مثال حل‌شده

``` text
config system global
    set admintimeout 10
    set admin-lockout-threshold 3
    set admin-lockout-duration 300
end
config system admin
    edit "mgr-hamed"
        set accprofile "super_admin_readonly"
        set trusthost1 192.168.90.0 255.255.255.0
    next
end
execute backup config sftp fgt-daily.conf 192.168.90.10 backup-user <PASSWORD>
```

(نام فیلدها/سینتکس `Unverified`.) **تست Restore:** Lab FGT هم‌نسخه، `execute restore config ...`، مقایسه Interface/Policy، ثبت RTO.

**مثال متوسط:** Backup با رمز در ریپو Commit شد. اقدام: حذف از تاریخچه، چرخش رمزها، Scan Secret (ابزار)، Prevention (pre-commit).

**مثال سخت:** پس از ارتقا Config ناسازگار؛ Rollback: Backup قبل از ارتقا، Firmware قبلی، تست.

### ۵) GUI و CLI

**GUI:** System → Administrators؛ System → Settings؛ System → Config → Backup/Restore؛ Log & Report → Events. **CLI:** مطابق مثال.

### ۶) نکات امنیتی

- حساب مشترک و رمز ضعیف ممنوع.
- Token API هرگز در Log/ریپو.
- Backup رمزشده.

### ۷) جمع‌بندی

- Hardening = کاهش سطح حمله + Least Privilege + MFA + Patch.
- Backup بدون تست Restore بی‌اعتبار.
- API با Trusted Host و Profile حداقلی.

### ۸) تمرین و ارزیابی

**ت1.** (ساده) چرا Telnet/HTTP غیرفعال شود؟ *(پاسخ: 27-7-ت1)*

**ت2.** (متوسط) تست Restore چگونه انجام می‌شود؟ *(پاسخ: 27-7-ت2)*

**ت3.** (سخت) چک‌لیست ۱۰ مورد Hardening با دلیل. *(پاسخ: 27-7-ت3)*

**ت4.** (سخت، طراحی) Token API برای مانیتورینگ را ایمن طراحی کنید. *(پاسخ: 27-7-ت4)*

**Q1.** Quick quiz (English): Why is an untested backup unreliable? *(پاسخ: 27-7-Q1)*

### ۹) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| RTO | Recovery Time Objective | زمان هدف بازیابی |
| Hardening | System hardening | امن‌سازی |
| Trusted host | Trusted host | IP مجاز |

- *Backups must be tested by restoring them.* ← Backupها باید با Restore تست شوند.

### ۱۰) منابع

- Fortinet: «Hardening your FortiOS» (مرجع رسمی؛ نسخه‌ی 7.0 را بررسی کنید)؛ CIS Fortinet FortiGate Benchmark؛ NIST SP 800-53 (CM، AU).

## پاسخ‌های فصل 27

> ابتدا بدون نگاه حل کنید. شناسه: درس-نوع+شماره (ت = تمرین، م = مرور).

**27-1-ت1** — Traffic Log؟

ترافیک.

**27-1-ت2** — Retention؟

نگهداری.

**27-1-م1** — چرا Retention؟

فضا.

**27-1-م2** — سناریو: Log قدیمی نیست؛ علت؟

Rotation.

**27-2-ت1** — SNMPv3؟

امن.

**27-2-ت2** — Template؟

قالب.

**27-2-م1** — چرا v3؟

رمز.

**27-2-م2** — سناریو: v2c باز؛ چه؟

v3/ACL.

**27-3-ت1** — Token؟

کلید.

**27-3-ت2** — Trusthost؟

محدود IP.

**27-3-م1** — چرا Trusthost؟

سطح حمله.

**27-3-م2** — سناریو: 401؛ علت؟

Trusthost.

**27-4-ت1** — Hardening؟

ایمن‌سازی.

**27-4-ت2** — Restore؟

تست.

**27-4-م1** — چرا تست Restore؟

Backup بی‌تست بی‌اعتبار.

**27-4-م2** — سناریو: Telnet باز؛ چه؟

غیرفعال.

**27-5-ت1** — G10؟

مانیتورینگ+Log+Hardening+Backup.

**27-5-ت2** — شاهد؟

لازم.

**27-5-م1** — چرا شاهد؟

اثبات.

**27-5-م2** — سناریو: بدون Backup؛ G10؟

شکست.


---

<a id="end9"></a>


### پاسخ‌های درس افزوده‌ی 27-0 (فصل 27)

**27-0-ت1** — Traffic، Event، UTM/Security.

**27-0-ت2** — تا انحراف را با مرجع عادی تشخیص دهیم و آستانه‌ی معنادار بگذاریم.

**27-0-ت3** — CPU>70٪ هشدار/90٪ بحرانی؛ Memory>80٪/90٪؛ Session>70٪/90٪ حد؛ Interface Error رشد؛ Tunnel/HA Down؛ Disk Log>80٪؛ همه بر پایه‌ی Baseline.

**27-0-ت4** — ۱۸۰ روز × ۲ GB = ۳۶۰ GB؛ + ۲۰٪ حاشیه؛ مرکزی با فشرده‌سازی و چرخش؛ هشدار فضا.

**27-0-Q1** — So events from different devices can be correlated reliably in time.


### پاسخ‌های درس افزوده‌ی 27-7 (فصل 27)

**27-7-ت1** — رمز و داده را بدون رمزنگاری می‌فرستند و قابل شنودند.

**27-7-ت2** — در Lab هم‌نسخه Restore، مقایسه Interface/Policy/Route، اندازه‌گیری RTO و ثبت.

**27-7-ت3** — تغییر admin پیش‌فرض، حساب شخصی، Trusted Host، allowaccess حداقل، غیرفعال Telnet/HTTP، MFA، Timeout/Lockout، Profile حداقلی، NTP، Patch.

**27-7-ت4** — حساب API با Profile Read-only، Trusted Host فقط مانیتورینگ، Token در Vault، چرخش دوره‌ای، Log تماس‌ها.

**27-7-Q1** — Because a backup that was never restored may be corrupt or incomplete, so recovery is not proven.

# پایان بخش ۹ (فصل‌های ۲۵ تا ۲۷)

## ۱) خلاصه‌ی مهارت‌های کسب‌شده
- اتصال FGT-CSR؛ مدیریت مرکزی و جایگزین بدون لایسنس؛ Syslog، SNMP، API، Hardening، Backup.

## ۲) آزمون پایان سه فصل
**س1** — Exstart در OSPF؟

**س2** — معادل show در FGT؟

**س3** — FMG؟

**س4** — FAZ؟

**س5** — جایگزین FAZ؟

**س6** — Backup بدون Secret؟

**س7** — SNMP امن؟

**س8** — Trusthost؟

**س9** — API Token؟

**س10** — Hardening؟

**س11** — Restore تست؟

**س12** — G10؟


## ۳) پاسخ آزمون
- **س1:** اغلب MTU mismatch.
- **س2:** get/diagnose.
- **س3:** مدیریت مرکزی.
- **س4:** Log مرکزی.
- **س5:** rsyslog.
- **س6:** حذف رمز.
- **س7:** v3.
- **س8:** محدودسازی IP.
- **س9:** کلید دسترسی.
- **س10:** ایمن‌سازی.
- **س11:** برای اعتبار Backup.
- **س12:** Monitoring+Log+Hardening+Backup.

## ۴) معیارهای تسلط
| مهارت | سطح | شاهد |
|---|---|---|
| Multi-vendor | L3 | A6 |
| مدیریت مرکزی | L2 | A9 |
| Ops/Hardening | L3 | G10 |

## ۵) مشکلات و موارد باقی‌مانده (صریح)
1. Labها اجرا نشده. 2. FMG/FAZ لایسنس. 3. API/SNMP سینتکس Unverified.

## ۶) پیش‌نیازهای بخش بعد
Backup همه‌ی Gateها؛ Wireshark/Sniffer مسلط.

## ۷) فهرست Lab و منابع مرتبط
کارت‌های Lab، `03-ops/*`

## ۸) وضعیت دوره
| مورد | مقدار |
|---|---|
| آخرین فصل تکمیل‌شده | ۲۷ |
| آخرین درس تکمیل‌شده | ۲۷-۶ |
| مهارت‌های تأییدشده | **هیچ‌کدام هنوز آزمون عملی واقعی نشده‌اند** (ممیزی/اجرای شما لازم است) |
| موضوعات نیازمند مرور | طبق «معیارهای تسلط» |
| فصل بعدی | ۲۸ |
| فایل تولیدشده | `course/Course_Part_09_Chapters_25-27.md` |
