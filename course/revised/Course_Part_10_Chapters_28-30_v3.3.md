# Enterprise Network & Security Engineering — دوره‌ی تخصصی Cisco و Enterprise Firewall
## بخش ۱۰ از ۱۱ — فصل‌های ۲۸ تا ۳۰

| مورد | مقدار |
|---|---|
| نام دوره | Enterprise Network & Security Engineering (Cisco + FortiGate) |
| شماره بخش | ۱۰ از ۱۱ |
| فصل‌های این فایل | ۲۸ ، ۲۹ ، ۳۰ |
| تاریخ تولید | ۲۰۲۶-۱۱-۲۶ |
| نسخه Blueprint | v3.0 (+ بازبینی ۱٫۱) |
| نسخه‌های نرم‌افزار | FortiOS 7.0.3 (اسمی؛ بوت‌نشده؛ تأیید با `get system status`) ؛ Cisco vIOS-L2 15.2(20200924، Experimental) ؛ Cisco vIOS 15.9(3)M9 ؛ VPCS ؛ PNetLab 4.2.8 ؛ ESXi 8.0U2 ؛ CSR1000v 17.03.02 (IOS-XE؛ آزمایش‌نشده) |
| وضعیت تکمیل | **فصل‌های ۲۸–۳۰ تولید شد؛ Packet Analysis، Blue Team/Lifecycle، Migration.** Labها «اجرا نشده»؛ دستورها آزمایش‌نشده. |

> **قوانین خواندن:** تمرین‌ها و پرسش‌های مرور بدون پاسخ‌اند؛ پاسخ در «پاسخ‌های فصل». «اجرا نشده» یعنی خروجی‌ها **پیش‌نیاز/پیش‌بینی** هستند. «CLI-Accepted» ≠ «کار می‌کند». رمزها نمونه‌اند.

### وضعیت راستی‌آزمایی Labهای این بخش
خلاصه: اجرا نشده (فقط طراحی): 13.

| Lab | وضعیت |
|---|---|
| 28-1 | اجرا نشده (فقط طراحی) |
| 28-2 | اجرا نشده (فقط طراحی) |
| 28-3 | اجرا نشده (فقط طراحی) |
| 28-4 | اجرا نشده (فقط طراحی) |
| 28-5 | اجرا نشده (فقط طراحی) |
| 29-1 | اجرا نشده (فقط طراحی) |
| 29-2 | اجرا نشده (فقط طراحی) |
| 29-3 | اجرا نشده (فقط طراحی) |
| 29-4 | اجرا نشده (فقط طراحی) |
| 30-1 | اجرا نشده (فقط طراحی) |
| 30-2 | اجرا نشده (فقط طراحی) |
| 30-3 | اجرا نشده (فقط طراحی) |
| 30-4 | اجرا نشده (فقط طراحی) |

---

<a id="ch28"></a>

> **نسخه v3.3:** این بخش در دسته‌های B/A/C بدون تغییر محتوایی است (فشرده‌تر از فصل‌های توسعه‌یافته؛ در دسته D بازنویسی می‌شود).

# فصل 28 — Packet Analysis و بلوک‌های عیب‌یابی

**مدت:** ۳۶ ساعت | **پیش‌نیاز:** فصل ۲، ۱۴.
**اهداف:** تحلیل بسته با Wireshark و Sniffer FortiGate؛ TCP Handshake، Retransmission، DNS، TLS؛ ده‌پرسش عیب‌یابی؛ بلوک‌های TS تکرارپذیر.
**اشتباهات رایج:** Filter بیش‌ازحد باز؛ تحلیل بدون Baseline؛ فراموشی Disable Debug.

**درس‌های فصل:**
- [درس 28-1 — Sniffer و Capture درست](#l-28-1)
- [درس 28-2 — TCP Handshake، Retransmission و DNS](#l-28-2)
- [درس 28-3 — TLS و Certificate در Capture](#l-28-3)
- [درس 28-4 — ده‌پرسش عیب‌یابی و بلوک TS](#l-28-4)
- [درس 28-5 — آزمون فصل ۲۸](#l-28-5)

---

<a id="l-28-1"></a>

## درس 28-0 — تحلیل بسته عمیق: TCP، DNS، TLS و الگوهای خرابی در Wireshark/Sniffer

**فصل ۲۸ · درس افزوده (پیش‌درس ۲۸-۱) · پیش‌نیاز: ۲-۰، ۱۴-۷، ۱۱-۷ · ≈ ۸ ساعت**

> **وضعیت:** خروجی‌ها نمونه‌ی آموزشی‌اند؛ Capture واقعی در Lab «اجرا نشده».

### ۱) هدف آموزشی

1. TCP را از روی بسته تحلیل کند: Handshake، Window، Retransmission، Dup ACK، RST، Zero Window.
2. الگوهای خرابی را تشخیص دهد: Drop، MTU/PMTUD، Asymmetric، Latency، Packet Loss.
3. DNS و TLS را در Capture بخواند (Query/Response، SNI، Alert).
4. Capture را درست بگیرد (نقطه، Filter، حجم) و با Sniffer FortiGate تکمیل کند.
5. از Capture تا RCA بنویسد.

### ۲) مفهوم پایه

بسته‌ها «حقیقت میدانی»اند: لاگ می‌گوید فایروال چه تصمیمی گرفت؛ Capture می‌گوید روی سیم چه گذشت. تحلیل = مقایسه‌ی دو نقطه‌ی Capture (قبل/بعد از دستگاه).

### ۳) توضیح عمیق فنی

#### ۳-۱) نقطه‌ی Capture

``` text
Client --[A]-- FW(in) FW(out) --[B]-- Server
A and B captures: compare which packet disappears and where
```

اگر بسته در A هست و در B نیست: دستگاه میانی (Policy/Route/Drop). اگر هست ولی پاسخ نیست: سرور/مسیر برگشت.

#### ۳-۲) الگوهای TCP

| الگو | معنی | علت‌های رایج |
|---|---|---|
| SYN بدون SYN/ACK | اتصال برقرار نمی‌شود | Policy، Route، پورت بسته، Asymmetric |
| SYN, RST | پورت بسته/رد | سرویس، Firewall |
| Retransmission | بسته‌ی گم‌شده | تلفات، MTU، Congestion |
| Dup ACK ×3 | Fast retransmit | Loss/Reordering |
| Zero Window | گیرنده پر | برنامه کند |
| ICMP Frag Needed | PMTUD | MTU کمتر در مسیر |
| فقط بزرگ‌ها قفل | PMTUD Black hole | ICMP Block/MTU |

``` text
RTT ~= time between SYN and SYN/ACK
Retransmission rate = retransmitted segments / total segments
```

#### ۳-۳) Wireshark: Filterهای مفید

``` text
tcp.analysis.retransmission
tcp.analysis.duplicate_ack
tcp.flags.syn==1 and tcp.flags.ack==0
tcp.analysis.zero_window
icmp.type==3 and icmp.code==4
dns.flags.rcode != 0
tls.alert_message
```

#### ۳-۴) DNS و TLS

- DNS: Query بدون Response (UDP Drop/سرور)، NXDOMAIN (نام)، Response کند (Latency).
- TLS: ClientHello با SNI؛ Alert `bad_certificate`/`unknown_ca` (CA/Pinning)؛ Handshake کند (RTT/CPU Inspection).

#### ۳-۵) Sniffer FortiGate

`diagnose sniffer packet <if> "<filter>" 4 <count> l` (verbose 4: IP+Interface؛ 6: Ethernet هم)؛ خروجی را به فایل و با اسکریپت به PCAP تبدیل کنید (ابزار fgt2eth)؛ روی Offloadشده ممکن است ناقص باشد (۱۲-۹).

### ۴) مثال حل‌شده

**پرونده:** دانلود ۵۰ MB از VPN در ۲٪ می‌ایستد. Capture در دو سر: بسته‌های بزرگ (1500 B) از A می‌روند و در B نمی‌رسند؛ ICMP Frag Needed بازگردانده نمی‌شود (ICMP توسط Firewall میانی Block). **RCA:** PMTUD Black hole. **رفع:** MSS Clamp (`tcp-mss`)، اجازه‌ی ICMP Type 3 Code 4. **تأیید:** Capture: بسته‌های ≤ MSS؛ دانلود کامل.

**مثال متوسط:** SYN→RST: سرور پورت را نمی‌شناسد؛ مقایسه با `telnet`. **مثال سخت:** Retransmission فقط یک جهت: مسیر برگشت تلفات دارد (Interface Error) → `get system interface physical`.

### ۵) GUI و CLI

**GUI:** Network → Diagnostics → Packet Capture؛ **CLI:** `diagnose sniffer packet any "host X and port Y" 6 100 l`.

### ۶) نکات امنیتی

- PCAP داده‌ی حساس دارد: محدود، رمزنگاری، حذف.
- Capture مجاز و مستند.

### ۷) جمع‌بندی

- دو نقطه‌ی Capture بسته‌ی گم‌شده را پیدا می‌کنند.
- الگوهای TCP علت را نشان می‌دهند.
- MTU/ICMP/Asymmetric سه علت شایع.

### ۸) تمرین و ارزیابی

**ت1.** (ساده) SYN بدون SYN/ACK یعنی چه؟ *(پاسخ: 28-0-ت1)*

**ت2.** (متوسط) PMTUD Black hole را توضیح دهید. *(پاسخ: 28-0-ت2)*

**ت3.** (سخت) Capture دو نقطه‌ای را برای یافتن Drop بنویسید. *(پاسخ: 28-0-ت3)*

**Q1.** Quick quiz (English): Which ICMP type and code signal fragmentation needed? *(پاسخ: 28-0-Q1)*

### ۹) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| PMTUD | Path MTU Discovery | کشف MTU مسیر |
| RTT | Round-Trip Time | زمان رفت و برگشت |
| PCAP | Packet capture | فایل بسته |
| Dup ACK | Duplicate ACK | ACK تکراری |

- *Capture at two points to locate where packets disappear.* ← در دو نقطه Capture بگیرید تا محل ناپدید شدن بسته‌ها پیدا شود.

### ۱۰) منابع

- Wireshark User's Guide (TCP analysis)؛ RFC 1191 (PMTUD)، RFC 9293 (TCP)، RFC 792 (ICMP).

## درس 28-1 — Sniffer و Capture درست

**فصل 28 - روز 1 · پیش‌نیاز: فصل ۲۷ · ۶ ساعت**

### ۱) معرفی درس

گرفتن بسته در FGT و Wireshark.

### ۲) پیش‌نیازها

فصل ۲۷

### ۳) توضیح مفهومی

- Sniffer verbose 4/6.
- Filter دقیق.
- ذخیره و تحلیل در Wireshark.
- PCAP بدون داده‌ی حساس.
- تعداد محدود.

### ۴) مثال ساده

دیدن بسته‌ها مثل فیلم کند.

### ۵) مثال سازمانی

سازمان: RCA با Capture.

### ۶) تصویر و توپولوژی

```text
Client -> FGT -> Server (capture at each point)
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. Network > Packet Capture.

#### روش خط فرمان (CLI)

```text
diagnose sniffer packet any "host 192.168.10.5 and port 443" 4 50 l
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- `Unverified`.

### ۸) تست عملکرد

- یک Capture بگیرید.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | Capture خالی |
| شواهد/دستور | Filter |
| علت | Interface |
| رفع | اصلاح |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** Verbose؟ *(پاسخ: 28-1-ت1)*

**ت2.** Filter؟ *(پاسخ: 28-1-ت2)*

### ۱۱) مرور و ارزیابی

**م1.** چرا Filter؟ *(پاسخ: 28-1-م1)*

**م2.** سناریو: Capture خالی؛ علت؟ *(پاسخ: 28-1-م2)*

**معیار تسلط:** Capture و تحلیل.

**اشتباهات رایج:** Filter باز.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| PCAP | Packet capture | فایل بسته | Wireshark |

| English sentence | ترجمه |
|---|---|
| Use narrow capture filters. | از Filter باریک استفاده کنید. |

#### کارت Lab — درس 28-1

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | Capture |
| 2 | پیش‌نیاز | فصل ۲۷ |
| 3 | توپولوژی | FGT+Client |
| 4 | تجهیزات | FGT |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | — |
| 7 | وضعیت اولیه | Baseline |
| 8 | صورت مسئله | Capture |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | sniffer |
| 11 | سناریوی خرابی | Capture خالی |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | فایل |
| 14 | معیار پذیرش | ثبت |
| 15 | مستندات نهایی | `03-ops/capture.md` |
| 16 | Cleanup و بازگردانی | — |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="l-28-2"></a>

## درس 28-2 — TCP Handshake، Retransmission و DNS

**فصل 28 - روز 2 · پیش‌نیاز: درس ۲۸-۰ · ۶ ساعت**

### ۱) معرفی درس

نشانه‌های رایج در بسته.

### ۲) پیش‌نیازها

درس ۲۸-۰

### ۳) توضیح مفهومی

- SYN/SYN-ACK/ACK.
- Retransmission=تلفات.
- RST.
- DNS Query/Response.
- Latency.

### ۴) مثال ساده

دیدن بسته‌ها مثل فیلم کند.

### ۵) مثال سازمانی

سازمان: RCA با Capture.

### ۶) تصویر و توپولوژی

```text
Client -> FGT -> Server (capture at each point)
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. Wireshark: Statistics.

#### روش خط فرمان (CLI)

```text
diagnose sniffer packet any "port 53" 4 20 l
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- `Unverified`.

### ۸) تست عملکرد

- تحلیل Handshake.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | SYN بی‌پاسخ |
| شواهد/دستور | capture |
| علت | Drop |
| رفع | Policy |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** RST؟ *(پاسخ: 28-2-ت1)*

**ت2.** Retransmission؟ *(پاسخ: 28-2-ت2)*

### ۱۱) مرور و ارزیابی

**م1.** چرا SYN بی‌پاسخ؟ *(پاسخ: 28-2-م1)*

**م2.** سناریو: RST فوری؛ علت؟ *(پاسخ: 28-2-م2)*

**معیار تسلط:** Capture و تحلیل.

**اشتباهات رایج:** Filter باز.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| RST | TCP Reset | ریست اتصال | TCP |

| English sentence | ترجمه |
|---|---|
| A SYN without a reply suggests a drop. | SYN بی‌پاسخ نشانه‌ی Drop است. |

#### کارت Lab — درس 28-2

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | TCP |
| 2 | پیش‌نیاز | درس ۲۸-۰ |
| 3 | توپولوژی | FGT+Client |
| 4 | تجهیزات | FGT |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | — |
| 7 | وضعیت اولیه | Baseline |
| 8 | صورت مسئله | Handshake |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | capture |
| 11 | سناریوی خرابی | SYN بی‌پاسخ |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | تحلیل |
| 14 | معیار پذیرش | ثبت |
| 15 | مستندات نهایی | `03-ops/tcp.md` |
| 16 | Cleanup و بازگردانی | — |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="l-28-3"></a>

## درس 28-3 — TLS و Certificate در Capture

**فصل 28 - روز 3 · پیش‌نیاز: درس ۲۸-۱ · ۶ ساعت**

### ۱) معرفی درس

Handshake TLS و خطاها.

### ۲) پیش‌نیازها

درس ۲۸-۱

### ۳) توضیح مفهومی

- ClientHello/ServerHello.
- SNI.
- Certificate.
- Alert.
- Inspection اثر.

### ۴) مثال ساده

دیدن بسته‌ها مثل فیلم کند.

### ۵) مثال سازمانی

سازمان: RCA با Capture.

### ۶) تصویر و توپولوژی

```text
Client -> FGT -> Server (capture at each point)
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. Wireshark: tls filter.

#### روش خط فرمان (CLI)

```text
diagnose sniffer packet any "port 443" 4 20 l
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- `Unverified`.

### ۸) تست عملکرد

- دیدن SNI.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | TLS Alert |
| شواهد/دستور | capture |
| علت | Cert |
| رفع | اصلاح |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** SNI؟ *(پاسخ: 28-3-ت1)*

**ت2.** Alert؟ *(پاسخ: 28-3-ت2)*

### ۱۱) مرور و ارزیابی

**م1.** چرا SNI؟ *(پاسخ: 28-3-م1)*

**م2.** سناریو: Alert؛ علت؟ *(پاسخ: 28-3-م2)*

**معیار تسلط:** Capture و تحلیل.

**اشتباهات رایج:** Filter باز.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| TLS | Transport Layer Security | رمزنگاری انتقال | Security |

| English sentence | ترجمه |
|---|---|
| SNI is visible in the ClientHello. | SNI در ClientHello دیده می‌شود. |

#### کارت Lab — درس 28-3

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | TLS |
| 2 | پیش‌نیاز | درس ۲۸-۱ |
| 3 | توپولوژی | FGT+Client |
| 4 | تجهیزات | FGT |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | — |
| 7 | وضعیت اولیه | Baseline |
| 8 | صورت مسئله | TLS |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | capture |
| 11 | سناریوی خرابی | TLS Alert |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | SNI |
| 14 | معیار پذیرش | ثبت |
| 15 | مستندات نهایی | `03-ops/tls.md` |
| 16 | Cleanup و بازگردانی | — |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="l-28-4"></a>

## درس 28-4 — ده‌پرسش عیب‌یابی و بلوک TS

**فصل 28 - روز 4 · پیش‌نیاز: درس ۲۸-۲ · ۶ ساعت**

### ۱) معرفی درس

چارچوب تکرارپذیر.

### ۲) پیش‌نیازها

درس ۲۸-۲

### ۳) توضیح مفهومی

- چه تغییر کرد؟
- کجا؟
- کدام لایه؟
- مسیر؟
- Policy؟
- NAT؟
- Session؟
- Log؟
- Capture؟
- RCA؟

### ۴) مثال ساده

دیدن بسته‌ها مثل فیلم کند.

### ۵) مثال سازمانی

سازمان: RCA با Capture.

### ۶) تصویر و توپولوژی

```text
Client -> FGT -> Server (capture at each point)
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. Log & Report.

#### روش خط فرمان (CLI)

```text
diagnose debug flow filter addr 192.168.20.11
diagnose debug flow trace start 5
diagnose debug enable
diagnose debug disable
diagnose debug reset
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- `Unverified`.
- Disable debug.

### ۸) تست عملکرد

- حل سه سناریو.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | RCA ناقص |
| شواهد/دستور | — |
| علت | سؤال جاافتاده |
| رفع | تکمیل |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** ده‌پرسش؟ *(پاسخ: 28-4-ت1)*

**ت2.** Debug flow؟ *(پاسخ: 28-4-ت2)*

### ۱۱) مرور و ارزیابی

**م1.** چرا چارچوب؟ *(پاسخ: 28-4-م1)*

**م2.** سناریو: بدون Log؛ چه؟ *(پاسخ: 28-4-م2)*

**معیار تسلط:** Capture و تحلیل.

**اشتباهات رایج:** Filter باز.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| TS | Troubleshooting | عیب‌یابی | Ops |

| English sentence | ترجمه |
|---|---|
| Use a repeatable troubleshooting framework. | از چارچوب عیب‌یابی تکرارپذیر استفاده کنید. |

#### کارت Lab — درس 28-4

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | TS Block |
| 2 | پیش‌نیاز | درس ۲۸-۲ |
| 3 | توپولوژی | FGT |
| 4 | تجهیزات | FGT |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | — |
| 7 | وضعیت اولیه | Baseline |
| 8 | صورت مسئله | ده‌پرسش |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | debug |
| 11 | سناریوی خرابی | RCA ناقص |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | RCA |
| 14 | معیار پذیرش | ثبت |
| 15 | مستندات نهایی | `03-ops/ts.md` |
| 16 | Cleanup و بازگردانی | — |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="l-28-5"></a>

## درس 28-5 — آزمون فصل ۲۸

**فصل 28 - روز 5 · پیش‌نیاز: درس ۲۸-۳ · ۶ ساعت**

### ۱) معرفی درس

ارزیابی.

### ۲) پیش‌نیازها

درس ۲۸-۳

### ۳) توضیح مفهومی

- Capture.
- TCP.
- TLS.
- TS.
- آزمون.

### ۴) مثال ساده

دیدن بسته‌ها مثل فیلم کند.

### ۵) مثال سازمانی

سازمان: RCA با Capture.

### ۶) تصویر و توپولوژی

```text
Client -> FGT -> Server (capture at each point)
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. Packet Capture.

#### روش خط فرمان (CLI)

```text
diagnose sniffer packet any "icmp" 4 10 l
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- `Unverified`.

### ۸) تست عملکرد

- حل آزمون.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | تحلیل غلط |
| شواهد/دستور | — |
| علت | — |
| رفع | — |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** Capture؟ *(پاسخ: 28-5-ت1)*

**ت2.** RCA؟ *(پاسخ: 28-5-ت2)*

### ۱۱) مرور و ارزیابی

**م1.** چرا شاهد؟ *(پاسخ: 28-5-م1)*

**م2.** سناریو: بدون Capture؛ چه؟ *(پاسخ: 28-5-م2)*

**معیار تسلط:** Capture و تحلیل.

**اشتباهات رایج:** Filter باز.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| RCA | Root Cause Analysis | علت ریشه‌ای | Ops |

| English sentence | ترجمه |
|---|---|
| Always attach evidence. | همیشه شاهد پیوست کنید. |

#### کارت Lab — درس 28-5

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | آزمون TS |
| 2 | پیش‌نیاز | درس ۲۸-۳ |
| 3 | توپولوژی | FGT |
| 4 | تجهیزات | FGT |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | — |
| 7 | وضعیت اولیه | Baseline |
| 8 | صورت مسئله | آزمون |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | capture |
| 11 | سناریوی خرابی | تحلیل غلط |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | سند |
| 14 | معیار پذیرش | ≥ ۴ از ۵ |
| 15 | مستندات نهایی | `03-ops/ts-exam.md` |
| 16 | Cleanup و بازگردانی | — |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="ans-28"></a>

## پاسخ‌های فصل 28

> ابتدا بدون نگاه حل کنید. شناسه: درس-نوع+شماره (ت = تمرین، م = مرور).

**28-1-ت1** — Verbose؟

سطح جزئیات.

**28-1-ت2** — Filter؟

محدودسازی.

**28-1-م1** — چرا Filter؟

حجم.

**28-1-م2** — سناریو: Capture خالی؛ علت؟

Interface.

**28-2-ت1** — RST؟

ریست.

**28-2-ت2** — Retransmission؟

تلفات.

**28-2-م1** — چرا SYN بی‌پاسخ؟

Drop.

**28-2-م2** — سناریو: RST فوری؛ علت؟

پورت بسته.

**28-3-ت1** — SNI؟

نام سرور.

**28-3-ت2** — Alert؟

خطا.

**28-3-م1** — چرا SNI؟

فیلتر.

**28-3-م2** — سناریو: Alert؛ علت؟

Cert.

**28-4-ت1** — ده‌پرسش؟

چارچوب.

**28-4-ت2** — Debug flow؟

مسیر بسته.

**28-4-م1** — چرا چارچوب؟

تکرارپذیری.

**28-4-م2** — سناریو: بدون Log؛ چه؟

Capture.

**28-5-ت1** — Capture؟

بسته.

**28-5-ت2** — RCA؟

ریشه.

**28-5-م1** — چرا شاهد؟

اثبات.

**28-5-م2** — سناریو: بدون Capture؛ چه؟

Log.


---

<a id="ch29"></a>


### پاسخ‌های درس افزوده‌ی 28-0 (فصل 28)

**28-0-ت1** — درخواست اتصال بی‌پاسخ: Drop/Policy/Route/پورت بسته یا Asymmetric.

**28-0-ت2** — بسته‌های بزرگ در مسیر با MTU کمتر نمی‌رسند و ICMP Frag Needed Block می‌شود؛ فرستنده اندازه را کم نمی‌کند و ارتباط قفل می‌شود.

**28-0-ت3** — Capture هم‌زمان قبل و بعد از دستگاه با Filter یکسان؛ مقایسه‌ی بسته‌ها؛ محل ناپدیدشدن همان نقطه‌ی مشکل است.

**28-0-Q1** — ICMP type 3 code 4.

# فصل 29 — Blue Team، Lifecycle و Vulnerability Management

**مدت:** ۳۶ ساعت | **پیش‌نیاز:** فصل ۲۷، ۲۸.
**اهداف:** تشخیص و پاسخ (Detection/Response)؛ Lifecycle دستگاه؛ Patch و Vulnerability؛ Threat Hunting ساده؛ Incident Report.
**هشدار:** فقط روی Lab ایزوله و مجاز. هیچ حمله‌ی واقعی بیرون از Lab.
**اشتباهات رایج:** Patch بدون Backup؛ Log ناقص؛ نبود Playbook.

**درس‌های فصل:**
- [درس 29-1 — Detection: Log و IOC ساده](#l-29-1)
- [درس 29-2 — Response و Playbook](#l-29-2)
- [درس 29-3 — Lifecycle، Patch و Vulnerability](#l-29-3)
- [درس 29-4 — Incident Report و آزمون](#l-29-4)

---

<a id="l-29-1"></a>

## درس 29-0 — Blue Team: Detection، Triage و چرخه‌ی پاسخ به حادثه (IR)

**فصل ۲۹ · درس افزوده (پیش‌درس ۲۹-۱) · پیش‌نیاز: ۲۷-۰، ۲۸-۰، ۱۱-۰ · ≈ ۶ ساعت**

> **وضعیت:** مفهومی؛ فقط روی Lab ایزوله و مجاز؛ هیچ حمله‌ی واقعی خارج از Lab.

### ۱) هدف آموزشی

1. چرخه‌ی **IR** (آماده‌سازی، تشخیص/تحلیل، مهار، ریشه‌کنی، بازیابی، درس‌آموخته) را اجرا کند.
2. از Log نشانه‌ی نفوذ (**IOC**) و الگوی رفتار (**TTP**) را تشخیص دهد.
3. **Triage** (اولویت‌بندی) و ثبت شواهد را انجام دهد.
4. Playbook برای سناریوهای رایج بنویسد.
5. تفاوت Detection و Prevention را در عمل بداند.

### ۲) مفهوم پایه

مهاجم باید فقط یک بار موفق شود؛ مدافع باید همیشه ببیند. Blue Team با **دید** (Log)، **هشدار**، **پاسخ** و **یادگیری** ریسک را مدیریت می‌کند. چارچوب مرجع: NIST SP 800-61 (چرخه‌ی IR) و MITRE ATT&CK (زبان مشترک TTP).

### ۳) توضیح عمیق فنی

#### ۳-۱) چرخه‌ی IR

``` text
1 Preparation        : tools, logs, playbooks, contacts, backups
2 Detection/Analysis : alerts, triage, scoping
3 Containment        : short-term (block) and long-term (isolate)
4 Eradication        : remove cause (malware, account, vulnerability)
5 Recovery           : restore, monitor
6 Lessons learned    : report, improve controls
```

#### ۳-۲) IOC و TTP

- **IOC:** IP/Domain/Hash/URL مخرب (قابل مسدودسازی ولی زودگذر).
- **TTP (Tactics, Techniques, Procedures):** رفتار (Scan، Brute-force، Lateral movement، Exfiltration) پایدارتر و ارزشمندتر.

مثال Detection از Firewall:

| الگو | داده | معنی |
|---|---|---|
| یک IP با Deny روی ده‌ها پورت | Traffic Log | Port Scan |
| Login ناموفق مکرر به VPN/Admin | Event Log | Brute-force |
| حجم بالای خروجی به یک IP ناشناس | Traffic Log (Bytes) | Exfiltration |
| DNS به دامنه‌ی نویزی/جدید | DNS Log | DGA/C2 |
| سرور DMZ به Internal (ممنوع) Deny | Traffic Log | حرکت جانبی |

#### ۳-۴) Triage

Severity = اثر × احتمال؛ پرسش‌ها: دارایی کدام است؟ موفق بود؟ داده خارج شد؟ مسیر گسترش؟ (**Scoping**).

#### ۳-۵) مهار با Firewall

Block IP (Address + Deny Policy بالای Policyها)، Quarantine، قطع VPN User، Clear Session (۱۳-۷). **قبل از مهار شواهد را ذخیره کنید** (Log، Capture).

### ۴) مثال حل‌شده

**سناریو:** Alert: ۴۰۰ Deny از 198.51.100.7 در ۲ دقیقه به پورت‌های 22,3389,445. **Triage:** Scan؛ موفق؟ Log Allow از همان IP؟ خیر. **مهار:** Address `BLOCK-IP` + Policy Deny بالا؛ Clear Session. **تحلیل:** منبع اینترنت؛ پورت‌های Management بسته‌اند. **درس:** Local-in WAN بسته (۱۲-۸).

``` text
config firewall address
    edit "BLOCK-198.51.100.7"
        set subnet 198.51.100.7 255.255.255.255
    next
end
```

(`Unverified`.)

**مثال سخت (Lateral movement):** PC کاربر Compromise شده و سعی می‌کند به DC SMB بزند؛ Segmentation Deny+Log؛ Alert؛ جداسازی PC؛ بازبینی اعتبارنامه‌ها؛ RCA.

### ۵) GUI و CLI

**GUI:** Log & Report؛ FortiView؛ Policy & Objects → Addresses. **CLI:** `execute log filter ...`، `diagnose sys session ...`.

### ۶) نکات امنیتی

- مهار بدون Evidence = از دست رفتن مدرک.
- ارتباط مستند و محدود؛ Change اضطراری ثبت.
- پس از حادثه Policyها و Patch بازبینی.

### ۷) جمع‌بندی

- IR شش فاز؛ Detection از TTP مهم‌تر از IOC.
- Triage و Scoping قبل از مهار.
- Evidence را حفظ کنید؛ درس‌آموخته را اعمال کنید.

### ۸) تمرین و ارزیابی

**ت1.** (ساده) شش فاز IR را بنویسید. *(پاسخ: 29-0-ت1)*

**ت2.** (متوسط) IOC و TTP چه فرقی دارند؟ *(پاسخ: 29-0-ت2)*

**ت3.** (سخت) Playbook Port Scan را بنویسید. *(پاسخ: 29-0-ت3)*

**ت4.** (سخت، طراحی) از Log فایروال سه Detection بسازید. *(پاسخ: 29-0-ت4)*

**Q1.** Quick quiz (English): Why preserve evidence before containment? *(پاسخ: 29-0-Q1)*

### ۹) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| IR | Incident Response | پاسخ به حادثه |
| IOC | Indicator of Compromise | نشانه‌ی نفوذ |
| TTP | Tactics, Techniques, Procedures | رفتار مهاجم |
| SOC | Security Operations Center | مرکز عملیات امنیت |

- *Contain first, but preserve the evidence.* ← مهار کنید ولی شواهد را حفظ کنید.

### ۱۰) منابع

- NIST SP 800-61 Rev.2 — Computer Security Incident Handling Guide؛ MITRE ATT&CK.

## درس 29-1 — Detection: Log و IOC ساده

**فصل 29 - روز 1 · پیش‌نیاز: فصل ۲۸ · ۶ ساعت**

### ۱) معرفی درس

چگونه حمله را ببینیم.

### ۲) پیش‌نیازها

فصل ۲۸

### ۳) توضیح مفهومی

- Log Deny زیاد.
- Port Scan.
- Login ناموفق.
- IOC ساده.
- Baseline.

### ۴) مثال ساده

نگهبان شبکه باید ببیند و پاسخ دهد.

### ۵) مثال سازمانی

سازمان: SOC کوچک با Log و Playbook.

### ۶) تصویر و توپولوژی

```text
FGT/Log -> Detection -> Response
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. Log & Report > Forward Traffic.

#### روش خط فرمان (CLI)

```text
execute log filter category 0
execute log display
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- `Unverified`.

### ۸) تست عملکرد

- شناسایی Scan.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | Alert کاذب |
| شواهد/دستور | Log |
| علت | Threshold |
| رفع | تنظیم |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** IOC؟ *(پاسخ: 29-1-ت1)*

**ت2.** Baseline؟ *(پاسخ: 29-1-ت2)*

### ۱۱) مرور و ارزیابی

**م1.** چرا Baseline؟ *(پاسخ: 29-1-م1)*

**م2.** سناریو: Scan؛ چه؟ *(پاسخ: 29-1-م2)*

**معیار تسلط:** Detection و Patch.

**اشتباهات رایج:** بدون Playbook.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| IOC | Indicator of Compromise | نشانه‌ی نفوذ | SOC |

| English sentence | ترجمه |
|---|---|
| Know your baseline. | وضعیت عادی را بشناسید. |

#### کارت Lab — درس 29-1

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | Detection |
| 2 | پیش‌نیاز | فصل ۲۸ |
| 3 | توپولوژی | FGT+Attacker-Lab |
| 4 | تجهیزات | FGT |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | — |
| 7 | وضعیت اولیه | Baseline |
| 8 | صورت مسئله | Scan |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | nmap |
| 11 | سناریوی خرابی | Alert کاذب |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | Log |
| 14 | معیار پذیرش | ثبت |
| 15 | مستندات نهایی | `03-ops/detect.md` |
| 16 | Cleanup و بازگردانی | — |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="l-29-2"></a>

## درس 29-2 — Response و Playbook

**فصل 29 - روز 2 · پیش‌نیاز: درس ۲۹-۰ · ۶ ساعت**

### ۱) معرفی درس

پاسخ گام‌به‌گام.

### ۲) پیش‌نیازها

درس ۲۹-۰

### ۳) توضیح مفهومی

- Contain.
- Eradicate.
- Recover.
- Lessons.
- Playbook.

### ۴) مثال ساده

نگهبان شبکه باید ببیند و پاسخ دهد.

### ۵) مثال سازمانی

سازمان: SOC کوچک با Log و Playbook.

### ۶) تصویر و توپولوژی

```text
FGT/Log -> Detection -> Response
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. Policy & Objects > Addresses.

#### روش خط فرمان (CLI)

```text
config firewall address
    edit "BLOCK-IP"
        set subnet 198.51.100.50 255.255.255.255
    next
end
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- `Unverified`.

### ۸) تست عملکرد

- Block IP.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | Block کار نمی‌کند |
| شواهد/دستور | Policy |
| علت | ترتیب |
| رفع | اصلاح |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** Contain؟ *(پاسخ: 29-2-ت1)*

**ت2.** Playbook؟ *(پاسخ: 29-2-ت2)*

### ۱۱) مرور و ارزیابی

**م1.** چرا Playbook؟ *(پاسخ: 29-2-م1)*

**م2.** سناریو: IP مشکوک؛ چه؟ *(پاسخ: 29-2-م2)*

**معیار تسلط:** Detection و Patch.

**اشتباهات رایج:** بدون Playbook.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| Playbook | Incident playbook | دستورالعمل پاسخ | SOC |

| English sentence | ترجمه |
|---|---|
| Write a playbook before incidents. | قبل از حادثه Playbook بنویسید. |

#### کارت Lab — درس 29-2

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | Response |
| 2 | پیش‌نیاز | درس ۲۹-۰ |
| 3 | توپولوژی | FGT |
| 4 | تجهیزات | FGT |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | — |
| 7 | وضعیت اولیه | Detect |
| 8 | صورت مسئله | Block |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | ping |
| 11 | سناریوی خرابی | Block کار نمی‌کند |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | Drop |
| 14 | معیار پذیرش | ثبت |
| 15 | مستندات نهایی | `03-ops/response.md` |
| 16 | Cleanup و بازگردانی | حذف |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="l-29-3"></a>

## درس 29-3 — Lifecycle، Patch و Vulnerability

**فصل 29 - روز 3 · پیش‌نیاز: درس ۲۹-۱ · ۶ ساعت**

### ۱) معرفی درس

مدیریت چرخه‌ی عمر.

### ۲) پیش‌نیازها

درس ۲۹-۱

### ۳) توضیح مفهومی

- End-of-Life.
- Patch.
- Advisory.
- CVE رایج (7.0.x).
- Backup/Rollback.

### ۴) مثال ساده

نگهبان شبکه باید ببیند و پاسخ دهد.

### ۵) مثال سازمانی

سازمان: SOC کوچک با Log و Playbook.

### ۶) تصویر و توپولوژی

```text
FGT/Log -> Detection -> Response
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. System > Firmware.

#### روش خط فرمان (CLI)

```text
get system status
execute backup config tftp pre-patch.conf 192.168.90.10
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- `Unverified`.

### ۸) تست عملکرد

- برنامه‌ی Patch.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | Patch شکست |
| شواهد/دستور | Backup |
| علت | — |
| رفع | Rollback |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** EoL؟ *(پاسخ: 29-3-ت1)*

**ت2.** Rollback؟ *(پاسخ: 29-3-ت2)*

### ۱۱) مرور و ارزیابی

**م1.** چرا Backup؟ *(پاسخ: 29-3-م1)*

**م2.** سناریو: 7.0.3 EoL؛ چه؟ *(پاسخ: 29-3-م2)*

**معیار تسلط:** Detection و Patch.

**اشتباهات رایج:** بدون Playbook.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| EoL | End of Life | پایان عمر | Lifecycle |

| English sentence | ترجمه |
|---|---|
| Track end-of-life dates. | تاریخ پایان عمر را پیگیری کنید. |

#### کارت Lab — درس 29-3

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | Patch |
| 2 | پیش‌نیاز | درس ۲۹-۱ |
| 3 | توپولوژی | FGT |
| 4 | تجهیزات | FGT |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | — |
| 7 | وضعیت اولیه | Baseline |
| 8 | صورت مسئله | Patch |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | status |
| 11 | سناریوی خرابی | Patch شکست |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | نسخه |
| 14 | معیار پذیرش | ثبت |
| 15 | مستندات نهایی | `03-ops/patch.md` |
| 16 | Cleanup و بازگردانی | Rollback |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="l-29-4"></a>

## درس 29-4 — Incident Report و آزمون

**فصل 29 - روز 4 · پیش‌نیاز: درس ۲۹-۲ · ۶ ساعت**

### ۱) معرفی درس

گزارش حادثه.

### ۲) پیش‌نیازها

درس ۲۹-۲

### ۳) توضیح مفهومی

- Timeline.
- Impact.
- RCA.
- Action.
- آزمون.

### ۴) مثال ساده

نگهبان شبکه باید ببیند و پاسخ دهد.

### ۵) مثال سازمانی

سازمان: SOC کوچک با Log و Playbook.

### ۶) تصویر و توپولوژی

```text
FGT/Log -> Detection -> Response
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. Log & Report.

#### روش خط فرمان (CLI)

```text
get system status
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- خواندنی.

### ۸) تست عملکرد

- گزارش یک‌صفحه‌ای.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | گزارش ناقص |
| شواهد/دستور | — |
| علت | — |
| رفع | تکمیل |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** Timeline؟ *(پاسخ: 29-4-ت1)*

**ت2.** Impact؟ *(پاسخ: 29-4-ت2)*

### ۱۱) مرور و ارزیابی

**م1.** چرا گزارش؟ *(پاسخ: 29-4-م1)*

**م2.** سناریو: بدون Timeline؛ مشکل؟ *(پاسخ: 29-4-م2)*

**معیار تسلط:** Detection و Patch.

**اشتباهات رایج:** بدون Playbook.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| Timeline | Incident timeline | خط زمان | SOC |

| English sentence | ترجمه |
|---|---|
| Write a blameless incident report. | گزارش حادثه را بدون سرزنش بنویسید. |

#### کارت Lab — درس 29-4

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | گزارش |
| 2 | پیش‌نیاز | درس ۲۹-۲ |
| 3 | توپولوژی | — |
| 4 | تجهیزات | — |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | — |
| 7 | وضعیت اولیه | — |
| 8 | صورت مسئله | گزارش |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | — |
| 11 | سناریوی خرابی | گزارش ناقص |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | سند |
| 14 | معیار پذیرش | ≥ ۴ از ۵ |
| 15 | مستندات نهایی | `03-ops/incident.md` |
| 16 | Cleanup و بازگردانی | — |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="ans-29"></a>

## پاسخ‌های فصل 29

> ابتدا بدون نگاه حل کنید. شناسه: درس-نوع+شماره (ت = تمرین، م = مرور).

**29-1-ت1** — IOC؟

نشانه‌ی نفوذ.

**29-1-ت2** — Baseline؟

وضعیت عادی.

**29-1-م1** — چرا Baseline؟

تشخیص انحراف.

**29-1-م2** — سناریو: Scan؛ چه؟

Block+Log.

**29-2-ت1** — Contain؟

مهار.

**29-2-ت2** — Playbook؟

دستورالعمل.

**29-2-م1** — چرا Playbook؟

سرعت.

**29-2-م2** — سناریو: IP مشکوک؛ چه؟

Block.

**29-3-ت1** — EoL؟

پایان پشتیبانی.

**29-3-ت2** — Rollback؟

بازگشت.

**29-3-م1** — چرا Backup؟

بازگشت.

**29-3-م2** — سناریو: 7.0.3 EoL؛ چه؟

ارتقا.

**29-4-ت1** — Timeline؟

زمان‌بندی.

**29-4-ت2** — Impact؟

اثر.

**29-4-م1** — چرا گزارش؟

یادگیری.

**29-4-م2** — سناریو: بدون Timeline؛ مشکل؟

RCA ناقص.


---

<a id="ch30"></a>


### پاسخ‌های درس افزوده‌ی 29-0 (فصل 29)

**29-0-ت1** — Preparation، Detection/Analysis، Containment، Eradication، Recovery، Lessons learned.

**29-0-ت2** — IOC نشانه‌ی مشخص و زودگذر (IP/Hash)؛ TTP رفتار و روش مهاجم و پایدارتر.

**29-0-ت3** — تشخیص Scan از Deny زیاد، بررسی Allow موفق، Block IP، Clear Session، بررسی Local-in، ثبت Evidence، PIR.

**29-0-ت4** — ۱) Deny چندپورتی از یک IP؛ ۲) Login ناموفق مکرر؛ ۳) حجم خروجی غیرعادی به IP ناشناس.

**29-0-Q1** — Because containment actions can alter or erase logs and sessions that are needed for analysis.

# فصل 30 — Migration: از Cisco ASA/Router به FortiGate (معماری ۸، G11)

**مدت:** ۳۶ ساعت | **پیش‌نیاز:** فصل ۱۳، ۲۷.
**اهداف:** برنامه‌ریزی مهاجرت؛ Inventory و Mapping Policy؛ Cutover و Rollback؛ تست پیش و پس. Gate G11: Plan کامل با Rollback و Evidence.
**هشدار:** Migration در تولید فقط با Change Window و تأیید؛ اینجا فقط Lab.
**اشتباهات رایج:** کپی بی‌فکر Rule؛ نبود Rollback؛ فراموشی NAT/Route.

**درس‌های فصل:**
- [درس 30-1 — Inventory و Mapping](#l-30-1)
- [درس 30-2 — Plan، Cutover و Rollback](#l-30-2)
- [درس 30-3 — تست پیش/پس و Evidence](#l-30-3)
- [درس 30-4 — Gate G11 و آزمون](#l-30-4)

---

<a id="l-30-1"></a>

## درس 30-0 — روش‌شناسی Migration: Inventory، نگاشت Policy، Cutover و Rollback

**فصل ۳۰ · درس افزوده (پیش‌درس ۳۰-۱) · پیش‌نیاز: ۱۳-۷، ۲۷-۷، ۲۵-۰ · ≈ ۶ ساعت**

> **وضعیت:** روش مستقل از برند؛ نگاشت قوانین ASA→FortiGate مفهومی و `Unverified`؛ فقط Lab.

### ۱) هدف آموزشی

1. مهاجرت را به‌صورت پروژه (Discovery، Design، Build، Test، Cutover، Stabilize) برنامه‌ریزی کند.
2. **Inventory** کامل و **Rule Hygiene** (حذف قوانین مرده/تکراری با Hit Count) انجام دهد.
3. نگاشت **Object، NAT، Route، VPN، Policy** را بنویسد و تفاوت مدل (ACL→Policy، NAT-order) را بفهمد.
4. **Cutover** با Rollback قابل‌اثبات طراحی کند.
5. آزمون پیش/پس و Evidence ثبت کند.

### ۲) مفهوم پایه

مهاجرت = تغییر پرخطر روی دستگاه حیاتی. «کپی کردن Rule» خطرناک است چون مدل پردازش فرق دارد (ترتیب NAT/ACL، Interface Security-level در برابر Zone، Implicit deny). موفقیت = **برابری رفتاری** (نه برابری متن Config) + **بازگشت امن**.

### ۳) توضیح عمیق فنی

#### ۳-۱) فازها

``` text
1 Discovery : inventory interfaces, routes, NAT, ACLs, VPNs, users, logs
2 Design    : target architecture, zone mapping, IP plan, rule cleanup
3 Build     : configure target in parallel (no traffic)
4 Test      : lab/pre-prod, positive & negative tests
5 Cutover   : change window, switch traffic, monitor
6 Stabilize : post-checks, hypercare, decommission after N days
```

#### ۳-۲) Rule Hygiene

با Hit Count و Log ۹۰ روزه: Ruleهای صفر-Hit، تکراری، Shadow، و Any-Any را شناسایی. هر Rule: صاحب، دلیل، تاریخ. **قبل از مهاجرت پاکسازی** کنید تا قوانین بد به سیستم جدید منتقل نشوند.

#### ۳-۳) نگاشت مفاهیم (مثال ASA→FortiGate؛ `Unverified`)

| ASA | FortiGate |
|---|---|
| nameif/security-level | Interface/Zone + Policy |
| access-list + access-group | Firewall Policy |
| object network/group | Address/Address Group |
| NAT (auto/twice) | Policy NAT/VIP/IP Pool/Central NAT |
| route | Static Route |
| crypto map | IPsec Phase1/2 (Route-based) |
| inspect (MPF) | Session Helper/Profile |

نکته: ASA به‌طور پیش‌فرض بین Interfaceهای با Security-level بالاتر→پایین‌تر اجازه می‌دهد؛ FortiGate Implicit deny؛ پس رفتار «بدون Rule» متفاوت است.

#### ۳-۴) Cutover

- **Change Window**، تیم، Rollback Trigger (مثلاً «۳۰ دقیقه بدون سرویس X»)، تماس.
- مراحل: Backup دو سو؛ جابه‌جایی Gateway/Route یا آدرس؛ ARP/Session؛ آزمون سرویس‌های حیاتی؛ مانیتورینگ.
- **Rollback:** بازگرداندن مسیر/کابل؛ Config قبلی؛ آزمون.

#### ۳-۵) Test Matrix

| سرویس | مبدأ | مقصد | انتظار | قبل | بعد |
|---|---|---|---|---|---|
| وب | Users | Internet | OK | ✓ | ✓ |
| ERP | Users | SRV | OK | ✓ | ✓ |
| ممنوع | Guest | SRV | Block | ✓ | ✓ |

### ۴) مثال حل‌شده

**پروژه:** جایگزینی ASA با FGT. Discovery: ۲۴۰ Rule، ۱۱۰ با Hit=0؛ پاکسازی ← ۱۱۰ Policy. Build موازی در Lab. Cutover: شب جمعه ۲۲:۰۰؛ Trigger Rollback ۳۰ دقیقه. شواهد: Test Matrix قبل/بعد. یک سرویس (FTP) خراب: Helper/Session ALG؛ رفع. Hypercare ۷ روز؛ Decommission ۳۰ روز.

**مثال سخت:** پس از Cutover فقط یک اپ کار نمی‌کند؛ ASA «twice NAT» ترتیب خاصی داشت؛ در FGT Policy NAT ناقص. **رفع:** VIP/IP Pool مناسب، Debug Flow.

### ۵) GUI و CLI

**GUI:** Policy & Objects؛ Log & Report. **CLI:** `diagnose firewall iprope lookup ...`، `diagnose debug flow ...`؛ Backup: `execute backup config ...`.

### ۶) نکات امنیتی

- Rule «موقت» هنگام مهاجمت را حذف کنید.
- Secretهای Config قدیمی منتقل نشوند.
- دستگاه قدیمی پس از Decommission پاک‌سازی امن.

### ۷) جمع‌بندی

- Inventory + Hygiene قبل از ساخت؛ برابری رفتاری هدف.
- Cutover بدون Rollback مجاز نیست.
- Test Matrix و Evidence.

### ۸) تمرین و ارزیابی

**ت1.** (ساده) فازهای Migration را بنویسید. *(پاسخ: 30-0-ت1)*

**ت2.** (متوسط) چرا Rule Hygiene قبل از مهاجرت؟ *(پاسخ: 30-0-ت2)*

**ت3.** (سخت) Rollback Trigger و روش آن را طراحی کنید. *(پاسخ: 30-0-ت3)*

**ت4.** (سخت، طراحی) Test Matrix برای ۱۰ سرویس بنویسید. *(پاسخ: 30-0-ت4)*

**Q1.** Quick quiz (English): Why aim for behavioral equivalence rather than copying rules? *(پاسخ: 30-0-Q1)*

### ۹) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Cutover | Cutover | سوئیچ نهایی |
| Hypercare | Hypercare | پایش ویژه پس از تغییر |
| Shadow rule | Shadowed rule | Rule پنهان‌شده |
| Hit count | Hit count | تعداد استفاده |

- *Clean up rules before migrating them.* ← قبل از مهاجرت قوانین را پاکسازی کنید.

### ۱۰) منابع

- NIST SP 800-41 Rev.1؛ ITIL 4 (Change Enablement)؛ Fortinet FortiConverter (مرجع رسمی؛ لایسنس/نسخه را بررسی کنید).

## درس 30-1 — Inventory و Mapping

**فصل 30 - روز 1 · پیش‌نیاز: فصل ۲۹ · ۶ ساعت**

### ۱) معرفی درس

ثبت وضعیت فعلی و نگاشت.

### ۲) پیش‌نیازها

فصل ۲۹

### ۳) توضیح مفهومی

- Interface، Route، NAT، Policy.
- Object Mapping.
- حذف Ruleهای مرده.
- Hit Count.
- سند.

### ۴) مثال ساده

جابجایی خانه با لیست.

### ۵) مثال سازمانی

سازمان: جایگزینی فایروال قدیمی.

### ۶) تصویر و توپولوژی

```text
Old FW -> New FGT (Cutover)
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. Policy & Objects.

#### روش خط فرمان (CLI)

```text
show running-config
get system interface
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- خواندنی.

### ۸) تست عملکرد

- Inventory.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | Rule جاافتاده |
| شواهد/دستور | diff |
| علت | Mapping |
| رفع | تکمیل |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** Mapping؟ *(پاسخ: 30-1-ت1)*

**ت2.** Hit count؟ *(پاسخ: 30-1-ت2)*

### ۱۱) مرور و ارزیابی

**م1.** چرا حذف Rule مرده؟ *(پاسخ: 30-1-م1)*

**م2.** سناریو: Rule ناشناخته؛ چه؟ *(پاسخ: 30-1-م2)*

**معیار تسلط:** Plan مهاجرت.

**اشتباهات رایج:** بدون Rollback.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| Hit count | Hit count | تعداد استفاده | FW |

| English sentence | ترجمه |
|---|---|
| Remove dead rules before migrating. | قبل از مهاجرت Ruleهای مرده را حذف کنید. |

#### کارت Lab — درس 30-1

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | Inventory |
| 2 | پیش‌نیاز | فصل ۲۹ |
| 3 | توپولوژی | Old+FGT |
| 4 | تجهیزات | — |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | — |
| 7 | وضعیت اولیه | — |
| 8 | صورت مسئله | Inventory |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | — |
| 11 | سناریوی خرابی | Rule جاافتاده |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | سند |
| 14 | معیار پذیرش | تأیید |
| 15 | مستندات نهایی | `02-design/mig-inventory.md` |
| 16 | Cleanup و بازگردانی | — |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="l-30-2"></a>

## درس 30-2 — Plan، Cutover و Rollback

**فصل 30 - روز 2 · پیش‌نیاز: درس ۳۰-۰ · ۶ ساعت**

### ۱) معرفی درس

برنامه‌ی تغییر ده‌مرحله‌ای.

### ۲) پیش‌نیازها

درس ۳۰-۰

### ۳) توضیح مفهومی

- Change Window.
- Pre-check.
- Cutover.
- Post-check.
- Rollback.

### ۴) مثال ساده

جابجایی خانه با لیست.

### ۵) مثال سازمانی

سازمان: جایگزینی فایروال قدیمی.

### ۶) تصویر و توپولوژی

```text
Old FW -> New FGT (Cutover)
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. System > Config.

#### روش خط فرمان (CLI)

```text
execute backup config tftp pre-cutover.conf 192.168.90.10
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- `Unverified`.

### ۸) تست عملکرد

- Plan.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | Cutover شکست |
| شواهد/دستور | Post-check |
| علت | — |
| رفع | Rollback |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** Rollback؟ *(پاسخ: 30-2-ت1)*

**ت2.** Pre-check؟ *(پاسخ: 30-2-ت2)*

### ۱۱) مرور و ارزیابی

**م1.** چرا Rollback؟ *(پاسخ: 30-2-م1)*

**م2.** سناریو: بعد از Cutover قطع؛ چه؟ *(پاسخ: 30-2-م2)*

**معیار تسلط:** Plan مهاجرت.

**اشتباهات رایج:** بدون Rollback.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| Cutover | Cutover | سوئیچ نهایی | Migration |

| English sentence | ترجمه |
|---|---|
| Always have a rollback plan. | همیشه Rollback Plan داشته باشید. |

#### کارت Lab — درس 30-2

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | Plan |
| 2 | پیش‌نیاز | درس ۳۰-۰ |
| 3 | توپولوژی | Old+FGT |
| 4 | تجهیزات | — |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | — |
| 7 | وضعیت اولیه | — |
| 8 | صورت مسئله | Plan |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | — |
| 11 | سناریوی خرابی | Cutover شکست |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | سند |
| 14 | معیار پذیرش | تأیید |
| 15 | مستندات نهایی | `02-design/mig-plan.md` |
| 16 | Cleanup و بازگردانی | — |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="l-30-3"></a>

## درس 30-3 — تست پیش/پس و Evidence

**فصل 30 - روز 3 · پیش‌نیاز: درس ۳۰-۱ · ۶ ساعت**

### ۱) معرفی درس

اثبات صحت.

### ۲) پیش‌نیازها

درس ۳۰-۱

### ۳) توضیح مفهومی

- Test Matrix.
- ping/traceroute/app.
- مقایسه Session.
- Evidence.
- RCA.

### ۴) مثال ساده

جابجایی خانه با لیست.

### ۵) مثال سازمانی

سازمان: جایگزینی فایروال قدیمی.

### ۶) تصویر و توپولوژی

```text
Old FW -> New FGT (Cutover)
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. Dashboard.

#### روش خط فرمان (CLI)

```text
diagnose sys session list
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- `Unverified`.

### ۸) تست عملکرد

- Test Matrix.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | تفاوت رفتار |
| شواهد/دستور | Matrix |
| علت | NAT |
| رفع | اصلاح |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** Matrix؟ *(پاسخ: 30-3-ت1)*

**ت2.** Evidence؟ *(پاسخ: 30-3-ت2)*

### ۱۱) مرور و ارزیابی

**م1.** چرا Matrix؟ *(پاسخ: 30-3-م1)*

**م2.** سناریو: یک اپ کار نمی‌کند؛ چه؟ *(پاسخ: 30-3-م2)*

**معیار تسلط:** Plan مهاجرت.

**اشتباهات رایج:** بدون Rollback.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| Matrix | Test matrix | جدول تست | Ops |

| English sentence | ترجمه |
|---|---|
| Compare before and after. | قبل و بعد را مقایسه کنید. |

#### کارت Lab — درس 30-3

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | Test Matrix |
| 2 | پیش‌نیاز | درس ۳۰-۱ |
| 3 | توپولوژی | Old+FGT |
| 4 | تجهیزات | FGT |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | — |
| 7 | وضعیت اولیه | Baseline |
| 8 | صورت مسئله | Matrix |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | ping |
| 11 | سناریوی خرابی | تفاوت رفتار |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | جدول |
| 14 | معیار پذیرش | ثبت |
| 15 | مستندات نهایی | `03-ops/mig-test.md` |
| 16 | Cleanup و بازگردانی | — |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="l-30-4"></a>

## درس 30-4 — Gate G11 و آزمون

**فصل 30 - روز 4 · پیش‌نیاز: درس ۳۰-۲ · ۶ ساعت**

### ۱) معرفی درس

ارزیابی.

### ۲) پیش‌نیازها

درس ۳۰-۲

### ۳) توضیح مفهومی

- Plan.
- Rollback.
- Evidence.
- RCA.
- آزمون.

### ۴) مثال ساده

جابجایی خانه با لیست.

### ۵) مثال سازمانی

سازمان: جایگزینی فایروال قدیمی.

### ۶) تصویر و توپولوژی

```text
Old FW -> New FGT (Cutover)
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

- اجرای G11.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | G11 ناقص |
| شواهد/دستور | — |
| علت | Rollback ندارد |
| رفع | تکمیل |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** G11؟ *(پاسخ: 30-4-ت1)*

**ت2.** Rollback؟ *(پاسخ: 30-4-ت2)*

### ۱۱) مرور و ارزیابی

**م1.** چرا شاهد؟ *(پاسخ: 30-4-م1)*

**م2.** سناریو: بدون Rollback؛ G11؟ *(پاسخ: 30-4-م2)*

**معیار تسلط:** Plan مهاجرت.

**اشتباهات رایج:** بدون Rollback.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| G11 | Gate 11 | دروازه‌ی ۱۱ | دوره |

| English sentence | ترجمه |
|---|---|
| A plan without rollback is incomplete. | Plan بدون Rollback ناقص است. |

#### کارت Lab — درس 30-4

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | آزمون G11 |
| 2 | پیش‌نیاز | درس ۳۰-۲ |
| 3 | توپولوژی | — |
| 4 | تجهیزات | — |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | — |
| 7 | وضعیت اولیه | — |
| 8 | صورت مسئله | G11 |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | — |
| 11 | سناریوی خرابی | G11 ناقص |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | شاهد |
| 14 | معیار پذیرش | ≥ ۴ از ۵ |
| 15 | مستندات نهایی | `03-ops/g11.md` |
| 16 | Cleanup و بازگردانی | — |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="ans-30"></a>

## پاسخ‌های فصل 30

> ابتدا بدون نگاه حل کنید. شناسه: درس-نوع+شماره (ت = تمرین، م = مرور).

**30-1-ت1** — Mapping؟

نگاشت.

**30-1-ت2** — Hit count؟

استفاده.

**30-1-م1** — چرا حذف Rule مرده؟

سادگی.

**30-1-م2** — سناریو: Rule ناشناخته؛ چه؟

Hit count.

**30-2-ت1** — Rollback؟

بازگشت.

**30-2-ت2** — Pre-check؟

پیش‌تست.

**30-2-م1** — چرا Rollback؟

ایمنی.

**30-2-م2** — سناریو: بعد از Cutover قطع؛ چه؟

Rollback.

**30-3-ت1** — Matrix؟

جدول تست.

**30-3-ت2** — Evidence؟

شاهد.

**30-3-م1** — چرا Matrix؟

کامل.

**30-3-م2** — سناریو: یک اپ کار نمی‌کند؛ چه؟

NAT/Policy.

**30-4-ت1** — G11؟

Plan+Rollback+Evidence.

**30-4-ت2** — Rollback؟

لازم.

**30-4-م1** — چرا شاهد؟

اثبات.

**30-4-م2** — سناریو: بدون Rollback؛ G11؟

شکست.


---

<a id="end10"></a>


### پاسخ‌های درس افزوده‌ی 30-0 (فصل 30)

**30-0-ت1** — Discovery، Design، Build، Test، Cutover، Stabilize.

**30-0-ت2** — تا قوانین مرده/تکراری/Any-Any منتقل نشوند و پیچیدگی/ریسک کم شود.

**30-0-ت3** — Trigger: ۳۰ دقیقه بدون سرویس حیاتی؛ روش: بازگرداندن Gateway/کابل و Config قبلی و آزمون.

**30-0-ت4** — جدول سرویس/مبدأ/مقصد/انتظار/قبل/بعد برای ۱۰ سرویس شامل آزمون منفی.

**30-0-Q1** — Because the processing models differ, and the goal is the same behavior, not the same text.

# پایان بخش ۱۰ (فصل‌های ۲۸ تا ۳۰)

## ۱) خلاصه‌ی مهارت‌های کسب‌شده
- Capture و تحلیل؛ Detection/Response؛ Patch/Lifecycle؛ برنامه‌ی Migration با Rollback.

## ۲) آزمون پایان سه فصل
**س1** — Sniffer verbose؟

**س2** — RST؟

**س3** — SNI؟

**س4** — ده‌پرسش؟

**س5** — IOC؟

**س6** — Playbook؟

**س7** — EoL؟

**س8** — Rollback؟

**س9** — Hit count؟

**س10** — Cutover؟

**س11** — Test Matrix؟

**س12** — G11؟


## ۳) پاسخ آزمون
- **س1:** سطح جزئیات.
- **س2:** ریست اتصال.
- **س3:** نام سرور در TLS.
- **س4:** چارچوب عیب‌یابی.
- **س5:** نشانه‌ی نفوذ.
- **س6:** دستورالعمل پاسخ.
- **س7:** پایان عمر.
- **س8:** بازگشت.
- **س9:** تعداد استفاده Rule.
- **س10:** سوئیچ نهایی.
- **س11:** جدول تست.
- **س12:** Plan+Rollback+Evidence.

## ۴) معیارهای تسلط
| مهارت | سطح | شاهد |
|---|---|---|
| Packet Analysis | L3 | آزمون فصل ۲۸ |
| Blue Team | L2 | فصل ۲۹ |
| Migration | L3 | G11 |

## ۵) مشکلات و موارد باقی‌مانده (صریح)
1. Labها اجرا نشده. 2. سینتکس Unverified. 3. هیچ حمله‌ی واقعی بیرون از Lab.

## ۶) پیش‌نیازهای بخش بعد
تمام Gateها (G1–G11) با شاهد؛ Backup.

## ۷) فهرست Lab و منابع مرتبط
کارت‌های Lab، `03-ops/*`

## ۸) وضعیت دوره
| مورد | مقدار |
|---|---|
| آخرین فصل تکمیل‌شده | ۳۰ |
| آخرین درس تکمیل‌شده | ۳۰-۶ |
| مهارت‌های تأییدشده | **هیچ‌کدام هنوز آزمون عملی واقعی نشده‌اند** (ممیزی/اجرای شما لازم است) |
| موضوعات نیازمند مرور | طبق «معیارهای تسلط» |
| فصل بعدی | ۳۱ |
| فایل تولیدشده | `course/Course_Part_10_Chapters_28-30.md` |
