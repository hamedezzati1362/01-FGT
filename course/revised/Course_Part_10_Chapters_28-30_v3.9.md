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

> **نسخه v3.9:** این بخش در دسته‌های B/A/C بدون تغییر محتوایی است (فشرده‌تر از فصل‌های توسعه‌یافته؛ در دسته D بازنویسی می‌شود).

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

## درس 28-1 — Capture درست: انتخاب نقطه، Filter، Sniffer FortiGate، PCAP، Offload و ملاحظات امنیت/قانون

**فصل 28 · بازنویسی عمیق · پیش‌نیاز: ۲۸-۰، ۱۴-۷، ۱۲-۹ · ≈ 8 ساعت**

> **وضعیت:** FortiOS 7.0.3 (بوت‌نشده)؛ خروجی‌ها نمونه‌ی آموزشی‌اند؛ دستورها `Unverified`؛ Lab «اجرا نشده».

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. از روی سؤال عیب‌یابی نقطه‌ی Capture (دو‌نقطه‌ای، قبل/بعد از NAT) را انتخاب کند.
2. Filter دقیق BPF و محدودیت حجم/زمان بنویسد.
3. Sniffer FortiGate (verbose، count، timestamp) را بخواند و به PCAP تبدیل کند.
4. تأثیر Offload/Interface مجازی را بر کامل بودن Capture بداند.
5. محدودیت‌های امنیتی/قانونی PCAP را رعایت کند.
6. Capture را در Wireshark با Display filter تحلیل اولیه کند.

### ۲) مفهوم پایه: چیست و چرا؟

Capture حقیقت میدانی است، ولی Capture بد (Filter باز، نقطه‌ی اشتباه، بدون زمان) مدت‌ها را هدر می‌دهد. اول سؤال، بعد نقطه، بعد Filter. و فراموش نکنید PCAP داده‌ی حساس (رمز، توکن، داده‌ی کاربر) دارد.

### ۳) توضیح عمیق فنی

#### ۱) از سؤال به نقطه

| سؤال | نقطه‌ها |
|---|---|
| بسته به فایروال می‌رسد؟ | Interface ورودی فایروال (یا SPAN بالاتر) |
| فایروال آن را عبور می‌دهد؟ | ورودی و خروجی همان فایروال |
| NAT چه کرد؟ | ورودی (آدرس اصلی) و خروجی (ترجمه‌شده) |
| سرور پاسخ می‌دهد؟ | روی سرور |
| مسیر برگشت متقارن است؟ | هر دو مسیر/فایروال |

#### ۲) Sniffer FortiGate

``` text
diagnose sniffer packet <interface|any> "<BPF filter>" <verbose> <count> <timestamp>
diagnose sniffer packet port2 "host 10.1.4.10 and tcp port 443" 4 100 l
```

- verbose: 1 هدر، 3 هدر+Hex، 4 هدر+Interface، 6 هدر+Hex+Interface+Ethernet (طبق مستند Fortinet؛ `Unverified` برای تفاوت‌ها).
- count: تعداد بسته؛ 0 تا Ctrl+C (خطرناک).
- `l` (local timestamp).

برای PCAP: خروجی verbose 3/6 را به فایل ذخیره و با ابزار تبدیل (fgt2eth.pl) به PCAP برسانید؛ یا Packet Capture GUI (Network → Diagnostics → Packet Capture) که مستقیماً PCAP می‌دهد.

#### ۳) Filter (BPF)

``` text
host 10.1.4.10
net 10.1.0.0/16
tcp port 443
udp port 53
icmp
"host 10.1.4.10 and not port 22"
"tcp[tcpflags] & (tcp-syn|tcp-rst) != 0"     # SYN or RST only
```

#### ۴) Offload و محدودیت‌ها

ترافیک Offloadشده (NPU) ممکن است در Sniffer دیده نشود/ناقص باشد (۱۲-۹). روی FortiGate-VM معمولاً NPU نیست. Capture روی Interface `any` ممکن است بسته را دو بار نشان دهد (ورود و خروج).

#### ۵) امنیت و قانون

PCAP شامل داده‌ی کاربران است: مجوز، حداقل زمان/حجم، ذخیره‌ی رمزشده، حذف پس از کار، عدم انتشار. TLS بدون Deep رمز می‌ماند ولی Header/SNI دیده می‌شود.

#### ۶) Wireshark

Display filter: `ip.addr==10.1.4.10`، `tcp.analysis.retransmission`، `tls.handshake.type==1`، `dns`. Statistics → Conversations/IO Graph/TCP Stream Graphs.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| نقطه‌ی Capture | دو‌نقطه‌ای |
| Filter | باریک؛ Count محدود |
| PCAP | موقت و رمزشده |
| Offload | آگاهی |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده):** Capture ping کلاینت↔سرور روی port2: `ip.addr` و `icmp`؛ Echo request/reply با زمان؛ RTT.

**متوسط (تحلیل):** وب باز نمی‌شود: Capture دو‌نقطه‌ای: روی port2 SYN دیده می‌شود؛ روی port1 نه. نتیجه: بسته داخل فایروال Drop شده (Policy/Route)؛ ادامه با Debug Flow. بدون Capture دوم فقط حدس بود.

**سخت (Offload/NAT):** Debug/Sniffer هیچ بسته‌ای نمی‌بیند ولی ترافیک جاری است: Offload. اقدام کنترل‌شده در Lab/Window: غیرفعال موقت Offload (در مدل‌های NPU) یا Capture روی نقطه‌ی بیرونی (سوئیچ/SPAN)؛ ثبت. همچنین NAT: ورودی src=10.1.4.10، خروجی src=203.0.113.10؛ تطبیق Flow با پورت مبدأ.

### ۶) پیاده‌سازی از مسیر GUI

1. Network → Diagnostics → Packet Capture: Interface، Filter، Packet count → Start → Download PCAP.
2. Wireshark: File → Open.

### ۷) پیاده‌سازی از مسیر CLI

``` text
diagnose sniffer packet port2 "host 10.1.4.10 and tcp port 443" 6 200 l
diagnose sniffer packet any "host 10.1.4.10 and port 53" 4 50 l
```

### ۸) Verification (اثبات صحت)

- PCAP قابل‌خواندن در Wireshark.
- مقایسه دو نقطه با Filter یکسان.
- حذف PCAP پس از کار.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| Capture خالی | Filter/Interface | Offload/Filter اشتباه |
| بسته‌ی تکراری | `any` | ورود+خروج |
| Timestamp نامعتبر | NTP | NTP |

### ۱۰) نکات امنیتی

- PCAP حساس؛ مجوز و حذف.
- عدم Capture بدون اجازه.

### ۱۱) جمع‌بندی مفهومی

- سؤال→نقطه→Filter.
- دو‌نقطه‌ای برای پیدا کردن محل Drop.
- Offload و NAT را در نظر بگیرید.
- امنیت PCAP.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) چرا Capture دو‌نقطه‌ای؟ *(پاسخ: 28-1-ت1)*

**ت2.** (ساده) verbose 4 چه نشان می‌دهد؟ *(پاسخ: 28-1-ت2)*

**ت3.** (متوسط) Filter برای فقط SYN/RST؟ *(پاسخ: 28-1-ت3)*

**ت4.** (متوسط) چرا `any` بسته‌ی تکراری نشان می‌دهد؟ *(پاسخ: 28-1-ت4)*

**ت5.** (سخت) Sniffer بسته‌ای نمی‌بیند ولی ترافیک می‌رود؛ تحلیل. *(پاسخ: 28-1-ت5)*

**ت6.** (سخت، طراحی) روش‌نامه‌ی Capture امن برای یک حادثه. *(پاسخ: 28-1-ت6)*

**Q1.** Quick quiz (English): Why should captures be taken at two points around the firewall? *(پاسخ: 28-1-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| BPF | Berkeley Packet Filter | زبان Filter بسته |
| PCAP | Packet capture file | فایل Capture |
| SPAN | Switched Port Analyzer | آینه‌ی پورت |

- *Use narrow capture filters.* ← از Filter باریک استفاده کنید.

### ۱۴) کارت Lab

**کارت Lab:** Capture. **وضعیت:** اجرا نشده. **Evidence:** `03-ops/capture.md`.

### ۱۵) منابع

- Wireshark User Guide
- Fortinet Docs: Packet capture / diagnose sniffer (7.0)
- tcpdump/pcap-filter manual

<a id="l-28-2"></a>

## درس 28-2 — تحلیل TCP و DNS در Capture: Handshake، Window، Retransmission، RTT، RST و الگوهای خرابی

**فصل 28 · بازنویسی عمیق · پیش‌نیاز: ۲۸-۰، ۲۸-۱، ۲-۰ · ≈ 9 ساعت**

> **وضعیت:** FortiOS 7.0.3 (بوت‌نشده)؛ خروجی‌ها نمونه‌ی آموزشی‌اند؛ دستورها `Unverified`؛ Lab «اجرا نشده».

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. فازهای TCP و فیلدهای مهم (Seq/Ack، Window، Flags، Options) را بخواند.
2. RTT، Retransmission rate، Zero Window، Dup ACK و RST را تفسیر کند.
3. DNS Query/Response (rcode، TTL، Latency) را تحلیل کند.
4. الگو را به علت (Drop، MTU، Congestion، برنامه) نگاشت کند.
5. با Wireshark Graphs محاسبات کمی انجام دهد.
6. گزارش تحلیل با شواهد بنویسد.

### ۲) مفهوم پایه: چیست و چرا؟

هر الگوی بسته یک «امضای خرابی» است. مهندس باید از روی الگو به علت برسد: «SYN بدون پاسخ» با «SYN→RST» و «Retransmission» سه علت متفاوت دارند.

### ۳) توضیح عمیق فنی

#### ۱) Handshake و RTT

``` text
t0 SYN ->           t1 <- SYN/ACK           t2 ACK ->
RTT_client_side = t2 - t0 (as seen at client)  ;  RTT_server_side = t1 - t0 (as seen at server)
```

در Capture روی فایروال: فاصله‌ی SYN تا SYN/ACK = RTT سمت سرور؛ SYN/ACK تا ACK = RTT سمت کلاینت (تقریباً).

#### ۲) نقشه‌ی الگو→علت

| الگو | معنی | علت‌های رایج |
|---|---|---|
| SYN بدون SYN/ACK | اتصال برقرار نمی‌شود | Policy/Route، پورت فیلتر، Asymmetric |
| SYN→RST | پورت بسته | سرویس خاموش |
| Retransmission | بسته‌ی گم‌شده | تلفات، MTU، Congestion |
| Dup ACK ×3 | Fast retransmit | Loss/Reordering |
| Zero Window | گیرنده پر | برنامه‌ی کند |
| RST وسط جلسه | قطع | فایروال/IPS/برنامه |
| ICMP 3/4 | Frag Needed | MTU |
| TCP Window Scale ناسازگار | Throughput کم | میانی دستکاری |

``` text
Retransmission rate = retransmitted segments / total segments
Throughput limit ~= Window / RTT     (e.g. 64 KB / 100 ms = 5.2 Mbit/s)
```

#### ۳) محدودیت Throughput (BDP)

``` text
BDP = bandwidth x RTT   (bytes in flight needed)
Example: 100 Mbit/s x 80 ms = 1 MB window needed; with 64 KB window -> ~6.5 Mbit/s
```

#### ۴) DNS

- Query بدون Response: UDP Drop/سرور.
- `rcode`: 0 OK، 2 SERVFAIL، 3 NXDOMAIN.
- Latency: زمان Query→Response.
- TTL و Cache؛ بزرگ‌بودن پاسخ و Fallback به TCP (EDNS0/MTU).

#### ۵) Filterهای Wireshark

``` text
tcp.analysis.retransmission  tcp.analysis.duplicate_ack  tcp.analysis.zero_window
tcp.flags.reset==1  icmp.type==3 and icmp.code==4
dns.flags.rcode != 0   dns.time > 0.2
```

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| Throughput | محاسبه‌ی BDP |
| DNS | Cache/Resolver |
| Capture | Filter+دو نقطه |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده):** Capture: SYN، SYN/ACK، ACK؛ RTT ≈ 22 ms؛ اتصال سالم.

**متوسط (محاسبه):** دانلود روی لینک 100 Mbps با RTT 80 ms فقط 6 Mbps. Window 64 KB ⇒ حد = 64KB/0.08 s ≈ 6.5 Mbit/s. علت: Window Scaling خاموش/دستکاری. رفع: فعال‌سازی Window Scale/بررسی میانی.

**سخت (چندعلتی):** دانلود VPN: Retransmission 3٪ و ICMP Frag Needed نیامده. تحلیل: PMTUD Black hole + Loss واقعی لینک؛ جدا‌سازی: ping DF اندازه‌ها (MTU)؛ Interface Errors (Loss)؛ رفع: MSS Clamp و رفع خطای لینک؛ اندازه‌گیری Retrans قبل/بعد.

### ۶) پیاده‌سازی از مسیر GUI

1. Wireshark: Statistics → TCP Stream Graphs (Time-Sequence، Throughput، RTT).
2. Statistics → Conversations/IO Graph.
3. Analyze → Expert Information.

### ۷) پیاده‌سازی از مسیر CLI

``` text
diagnose sniffer packet any "host 10.1.4.10 and tcp" 4 300 l
```

### ۸) Verification (اثبات صحت)

- جدول RTT/Retrans/Window.
- نمودار Time-Sequence.
- مقایسه‌ی قبل/بعد رفع.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| SYN بی‌پاسخ | Capture | Policy/Route |
| Retransmission | Interface errors | Loss/MTU |
| کند با Window کم | Window scale | Scaling/BDP |
| DNS کند | dns.time | Resolver |

### ۱۰) نکات امنیتی

- PCAP حساس.

### ۱۱) جمع‌بندی مفهومی

- الگو→علت.
- RTT و BDP محاسبه می‌شود.
- Retrans rate شاخص کیفیت.
- DNS rcode/Latency.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) SYN→RST یعنی چه؟ *(پاسخ: 28-2-ت1)*

**ت2.** (ساده) Zero Window چیست؟ *(پاسخ: 28-2-ت2)*

**ت3.** (متوسط) Window 64 KB و RTT 100 ms: حد Throughput؟ *(پاسخ: 28-2-ت3)*

**ت4.** (متوسط) BDP برای 100 Mbps و 80 ms؟ *(پاسخ: 28-2-ت4)*

**ت5.** (سخت) Retrans 3٪ + MTU مشکوک؛ جداسازی دو علت. *(پاسخ: 28-2-ت5)*

**ت6.** (سخت، طراحی) گزارش تحلیل Capture را با ساختار بنویسید. *(پاسخ: 28-2-ت6)*

**Q1.** Quick quiz (English): How does window size limit TCP throughput? *(پاسخ: 28-2-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| BDP | Bandwidth-delay product | حاصل‌ضرب پهنای باند و تأخیر |
| RTT | Round-trip time | زمان رفت و برگشت |
| Window scaling | TCP window scaling | مقیاس Window |

- *Patterns in packets point to specific causes.* ← الگوها در بسته‌ها به علت‌های مشخص اشاره می‌کنند.

### ۱۴) کارت Lab

**کارت Lab:** TCP. **وضعیت:** اجرا نشده. **Evidence:** `03-ops/tcp.md`.

### ۱۵) منابع

- RFC 9293
- RFC 7323 (Window Scale)
- Wireshark docs

<a id="l-28-3"></a>

## درس 28-3 — TLS در Capture: Handshake، SNI، Certificate، Alert، TLS 1.3 و اثر Inspection

**فصل 28 · بازنویسی عمیق · پیش‌نیاز: ۲۸-۰، ۱۶-۰، ۱۶-۵ · ≈ 8 ساعت**

> **وضعیت:** FortiOS 7.0.3 (بوت‌نشده)؛ خروجی‌ها نمونه‌ی آموزشی‌اند؛ دستورها `Unverified`؛ Lab «اجرا نشده».

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. Handshake TLS 1.2/1.3 را در Capture بخواند.
2. SNI، Cipher، Certificate chain و Alertها را تفسیر کند.
3. اثر Deep Inspection را در Capture (Issuer) اثبات کند.
4. QUIC/ECH و محدودیت دید را بشناسد.
5. مشکلات Pinning/CA/Cipher را عیب‌یابی کند.

### ۲) مفهوم پایه: چیست و چرا؟

TLS اکثر ترافیک را می‌پوشاند؛ ولی Handshake اطلاعات زیادی (SNI، نسخه، Cipher، گاهی گواهی) آشکار می‌کند. Capture TLS به شما می‌گوید «کجا شکست خورد» و «چه کسی دخالت کرد».

### ۳) توضیح عمیق فنی

#### ۱) Handshake

``` text
TLS 1.2: ClientHello(SNI,versions,ciphers) -> ServerHello, Certificate, ServerKeyExchange -> ClientKeyExchange, Finished
TLS 1.3: ClientHello(SNI, key_share) -> ServerHello(key_share) + {EncryptedExtensions, Certificate, Finished} encrypted
```

در 1.3 گواهی رمز است؛ فقط SNI/ClientHello دیده می‌شود (مگر ECH).

#### ۲) Alertها

| Alert | معنی | علت |
|---|---|---|
| unknown_ca | CA ناشناخته | CA فایروال نصب نیست |
| bad_certificate | گواهی بد | Pinning/نام |
| certificate_expired | منقضی | تاریخ |
| handshake_failure | Cipher/نسخه | ناسازگاری |
| protocol_version | نسخه | قدیمی |

#### ۳) اثبات Inspection

``` text
openssl s_client -connect example.com:443 -servername example.com 2>/dev/null | openssl x509 -noout -issuer
```

Issuer = CA فایروال ⇒ Deep Inspection فعال؛ Issuer = CA عمومی ⇒ بدون رمزگشایی.

#### ۴) QUIC و ECH

QUIC (UDP 443) با TLS 1.3؛ Deep Inspection سخت؛ سیاست بلاک QUIC. ECH SNI را رمز می‌کند؛ Web Filter بر پایه‌ی SNI کور می‌شود (آینده).

#### ۵) فیلترها

``` text
tls.handshake.type == 1            # ClientHello
tls.handshake.extensions_server_name
tls.alert_message
tls.handshake.certificate
quic
```

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| QUIC | بلاک تا TCP/TLS |
| Pinning | Exemption |
| Cipher | حداقل TLS 1.2 |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده):** ClientHello با SNI=example.com؛ ServerHello TLS1.3؛ Application Data.

**متوسط (تحلیل):** Alert `unknown_ca` فقط برای یک برنامه: CA فایروال در Trust Store آن برنامه نیست (Java/Firefox)؛ رفع: نصب CA یا Exemption.

**سخت (طراحی):** پس از فعال‌کردن Deep Inspection، برنامه‌ی بانکی Alert می‌دهد (Pinning). تحلیل: گواهی ارائه‌شده با Pin مطابق نیست؛ راه: Exemption آن FQDN/Category؛ ثبت؛ آزمون منفی: سایر سایت‌ها هنوز Inspect می‌شوند (Issuer).

### ۶) پیاده‌سازی از مسیر GUI

1. Wireshark: Filter tls؛ Statistics → Protocol Hierarchy.

### ۷) پیاده‌سازی از مسیر CLI

``` text
openssl s_client -connect example.com:443 -servername example.com
diagnose sniffer packet any "host 10.1.4.10 and tcp port 443" 4 100 l
```

### ۸) Verification (اثبات صحت)

- Issuer مقایسه.
- SNI در ClientHello.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| unknown_ca | Alert | CA/Store |
| handshake_failure | Cipher/نسخه | سازگاری |
| QUIC دور می‌زند | UDP 443 | بلاک |

### ۱۰) نکات امنیتی

- PCAP؛ Exemption مستند.

### ۱۱) جمع‌بندی مفهومی

- TLS1.3 گواهی رمز.
- Alertها علت را می‌گویند.
- Issuer اثبات Inspection.
- QUIC/ECH محدودیت دید.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) SNI چیست و کجا دیده می‌شود؟ *(پاسخ: 28-3-ت1)*

**ت2.** (ساده) چرا در TLS 1.3 گواهی دیده نمی‌شود؟ *(پاسخ: 28-3-ت2)*

**ت3.** (متوسط) unknown_ca چه می‌گوید؟ *(پاسخ: 28-3-ت3)*

**ت4.** (متوسط) چگونه Inspection را اثبات می‌کنید؟ *(پاسخ: 28-3-ت4)*

**ت5.** (سخت) برنامه‌ی Pinned خطا می‌دهد؛ تصمیم. *(پاسخ: 28-3-ت5)*

**ت6.** (سخت، طراحی) سیاست QUIC/ECH سازمان. *(پاسخ: 28-3-ت6)*

**Q1.** Quick quiz (English): Which command-line tool can show the issuer of the certificate presented through a firewall? *(پاسخ: 28-3-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| ECH | Encrypted Client Hello | رمزکردن ClientHello |
| Pinning | Certificate pinning | پین‌کردن گواهی |
| QUIC | QUIC transport | انتقال روی UDP |

- *The certificate issuer reveals whether inspection is active.* ← Issuer گواهی نشان می‌دهد Inspection فعال است یا نه.

### ۱۴) کارت Lab

**کارت Lab:** TLS. **وضعیت:** اجرا نشده. **Evidence:** `03-ops/tls.md`.

### ۱۵) منابع

- RFC 8446
- RFC 6066
- Wireshark TLS docs

<a id="l-28-4"></a>

## درس 28-4 — ده‌پرسش عیب‌یابی و بلوک‌های TS: چارچوب، سه پرونده‌ی کامل و کتابخانه‌ی TS

**فصل 28 · بازنویسی عمیق · پیش‌نیاز: ۱۴-۷، ۲۸-۱ تا ۲۸-۳ · ≈ 9 ساعت**

> **وضعیت:** FortiOS 7.0.3 (بوت‌نشده)؛ خروجی‌ها نمونه‌ی آموزشی‌اند؛ دستورها `Unverified`؛ Lab «اجرا نشده».

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. چارچوب ده‌پرسش را برای هر مشکل اجرا کند.
2. بلوک TS با فرضیه‌های رتبه‌بندی‌شده و شواهد بنویسد.
3. سه پرونده‌ی کامل (VPN، HTTPS کند، MTU) را حل و RCA کند.
4. کتابخانه‌ی TS قابل‌استفاده‌ی مجدد بسازد.
5. مقایسه‌ی شواهد و رد فرضیه را تمرین کند.

### ۲) مفهوم پایه: چیست و چرا؟

چارچوب ثابت سرعت و کیفیت می‌دهد. بلوک TS = «دانش تیم» به شکل قابل‌تکرار.

### ۳) توضیح عمیق فنی

#### ۱) ده پرسش

1 چه تغییر کرد؟ 2 چه کسی/چه سرویسی؟ 3 از کی؟ 4 کدام لایه؟ 5 بسته به فایروال می‌رسد؟ 6 Route؟ 7 Policy؟ 8 NAT/Session؟ 9 Profile/Inspection؟ 10 بسته خارج می‌شود و برمی‌گردد؟

#### ۲) قالب TS

``` text
ID / Date / Owner
Symptom: ...   Scope: who/what/since   Last change: ...
Evidence log: (time, command, output snippet)
Hypotheses ranked: H1 (likelihood, cheap test) ...
Tests & results -> accepted/rejected
Root cause
Fix + verification (positive and negative)
Prevention + owner/date
```

#### ۳) رتبه‌بندی فرضیه

``` text
Priority ~= likelihood x impact / test cost
```

اول فرضیه‌های محتمل و ارزان (ping/Policy/Route) بعد گران (Capture عمیق).

#### ۴) پرونده‌ها

**پرونده A: VPN Up ولی ترافیک نه.** شواهد: Bytes out>0، in=0؛ Debug Flow سمت مقابل Denied policy 0. علت: Policy سمت مقابل. رفع: Policy؛ آزمون مثبت/منفی؛ پیشگیری: چک‌لیست دوطرفه.

**پرونده B: HTTPS کند.** شواهد: CPU 85٪، `sys top` ipsengine؛ TLS Handshake طولانی. علت: IPS+Deep روی همه. رفع: Sensor انتخابی؛ Baseline بعد.

**پرونده C: بزرگ‌ها قفل.** شواهد: ping DF 1372 شکست؛ Retrans؛ نبود ICMP 3/4. علت: MTU/PMTUD. رفع: MSS Clamp 1360 و ICMP؛ تأیید.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| قالب TS | یکسان برای تیم |
| کتابخانه | نسخه‌دار |
| بازبینی | فصلی |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده):** پرونده A با بلوک TS کامل؛ زمان رفع ۱۲ دقیقه.

**متوسط (تحلیل):** پرونده B: دو علت هم‌زمان: Profile و Interface errors؛ جدا‌سازی با شواهد؛ رفع جداگانه و اندازه‌گیری.

**سخت (چندلایه):** پرونده C همراه با Asymmetric جزئی (۵٪ Flow). بلوک TS: H1 MTU (آزمون ping DF)، H2 Asymmetric (Sniffer)؛ هر دو تأیید؛ رفع دو علت؛ پیشگیری: استاندارد MTU و Route متقارن.

### ۷) پیاده‌سازی از مسیر CLI

``` text
diagnose debug flow filter addr 10.1.4.10
diagnose debug flow trace start 20
diagnose debug enable
diagnose debug disable
diagnose debug reset
get system performance status
```

### ۸) Verification (اثبات صحت)

- سه TS Block کامل با Evidence.
- کتابخانه‌ی TS.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| فرضیه ثابت نمی‌شود | آزمون | رد/بعدی |
| دو علت | شواهد جدا | رفع جدا |

### ۱۰) نکات امنیتی

- Debug را Disable کنید.
- Evidence بدون Secret.

### ۱۱) جمع‌بندی مفهومی

- ده پرسش + TS Block.
- رتبه‌بندی فرضیه.
- چندعلتی را جدا کنید.
- کتابخانه‌ی دانش.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) ده پرسش را فهرست کنید. *(پاسخ: 28-4-ت1)*

**ت2.** (ساده) چرا Debug را Disable می‌کنیم؟ *(پاسخ: 28-4-ت2)*

**ت3.** (متوسط) فرضیه‌ها را چگونه رتبه می‌دهید؟ *(پاسخ: 28-4-ت3)*

**ت4.** (متوسط) پرونده A: Bytes in=0؛ علت‌های ممکن؟ *(پاسخ: 28-4-ت4)*

**ت5.** (سخت) پرونده با دو علت هم‌زمان؛ روش جداسازی. *(پاسخ: 28-4-ت5)*

**ت6.** (سخت، طراحی) ساختار کتابخانه‌ی TS برای تیم. *(پاسخ: 28-4-ت6)*

**Q1.** Quick quiz (English): Why rank hypotheses by likelihood and test cost? *(پاسخ: 28-4-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| TS block | Troubleshooting block | قالب عیب‌یابی |
| Hypothesis | Hypothesis | فرضیه |

- *Keep an evidence log for every incident.* ← برای هر حادثه Evidence Log نگه دارید.

### ۱۴) کارت Lab

**کارت Lab:** TS. **وضعیت:** اجرا نشده. **Evidence:** `03-ops/ts.md`.

### ۱۵) منابع

- درس ۱۴-۷
- ITIL Problem Management

<a id="l-28-5"></a>

## درس 28-5 — آزمون عملی فصل ۲۸: تحلیل سه PCAP و RCA — صورت مسئله، کلید پاسخ و Rubric

**فصل 28 · بازنویسی عمیق · پیش‌نیاز: ۲۸-۱ تا ۲۸-۴، ۱۴-۲ · ≈ 12 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ سناریو و کلید پاسخ آموزشی‌اند؛ Lab «اجرا نشده»؛ دستورها `Unverified` تا اجرای Lab؛ ویژگی‌های وابسته به لایسنس مشخص شده‌اند.

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. سه PCAP را با Display Filter تحلیل کند.
2. الگوهای SYN-بی‌پاسخ، Retransmission/MTU و DNS/TLS شکست را تشخیص دهد.
3. برای هر PCAP RCA بنویسد.
4. رفع پیشنهادی و آزمون تأیید را بنویسد.
5. Evidence با شماره‌ی بسته ثبت کند.

### ۲) مفهوم پایه: چیست و چرا؟

PCAP بی‌طرف‌ترین شاهد است. دو مهندس بر سر علت بحث می‌کنند؛ یک فایل PCAP حکم می‌دهد. ولی تنها وقتی که بدانید چه را در آن ببینید. این آزمون سه الگوی کلاسیک را می‌سنجد.

### ۳) توضیح عمیق فنی

#### ۱) صورت مسئله

سه فایل: `case1.pcap` (سایت باز نمی‌شود)، `case2.pcap` (دانلود می‌ایستد)، `case3.pcap` (HTTPS خطا). برای هرکدام: الگو، علت، رفع، آزمون.

#### ۲) فیلترهای پایه

``` text
tcp.flags.syn==1 && tcp.flags.ack==0
tcp.analysis.retransmission
tcp.flags.reset==1
icmp.type==3 && icmp.code==4
dns.flags.rcode != 0
tls.alert_message
```

#### ۳) کلید

**Case 1:** ۵ بسته SYN از کلاینت با Retransmit (۱، ۳، ۷ ثانیه) و هیچ SYN-ACK. علت: مقصد/Firewall سرور SYN را نمی‌پذیرد یا مسیر برگشت. رفع: بررسی Policy/Route/سرور؛ Capture در مقصد.

**Case 2:** Handshake و چند بسته‌ی کوچک ok؛ بسته‌ی بزرگ (1514 بایت) Retransmit مکرر؛ ICMP نوع 3 کد 4 در جهت مخالف یا غایب. علت: MTU مسیر کمتر. رفع: MSS-clamp/اجازه‌ی ICMP.

**Case 3:** TLS Handshake: ClientHello سپس Alert (fatal) `certificate_unknown` یا `handshake_failure`. علت: گواهی نامعتبر/Inspection/SNI. رفع: گواهی CA مورد اعتماد کلاینت، یا Exempt در SSL Inspection.

#### ۴) قالب Evidence

``` text
case: 2
frames: 41-58 (large segments retransmitted), 60 (ICMP 3/4)
finding: PMTU 1400 ; MSS 1460
fix: tcp-mss 1360 ; allow ICMP frag-needed
verify: download 100MB x3 without retransmission
```

#### ۵) Rubric

الگوی هر Case ۱۵×۳، RCA ۲۰، رفع و آزمون ۱۵، Evidence با شماره‌ی بسته ۱۵، صداقت ۵. قبولی ۷۵.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| فیلتر | دقیق |
| ثبت | شماره بسته |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده):** Case 1: فقط SYN. نتیجه: پاسخی نیامده؛ مسیر/سرور.

**متوسط (Case 2):** بسته‌ی ۱۵۱۴ بایتی با DF Retransmit؛ بسته‌های ≤ ۱۴۰۰ می‌رسد؛ PMTU≈1400؛ رفع MSS 1360؛ آزمون دانلود.

**سخت (Case 3):** TLS Alert certificate_unknown پس از ServerHello/Certificate. مراحل: ۱) Certificate در frame 12؛ Issuer ناشناخته. ۲) علت: SSL Inspection با CA داخلی که روی کلاینت نصب نیست. ۳) رفع: نصب CA یا Exempt. ۴) آزمون: Handshake کامل.

### ۷) پیاده‌سازی از مسیر CLI

``` text
tcp.flags.syn==1 && tcp.flags.ack==0
tcp.analysis.retransmission
tls.alert_message
```

### ۸) Verification (اثبات صحت)

- شماره بسته‌ها در Evidence.
- آزمون پس از رفع.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| SYN بی‌پاسخ | مقصد/Firewall | Capture دو سمت |
| بزرگ می‌ایستد | MTU | MSS |
| TLS alert | گواهی | CA/Exempt |

### ۱۰) نکات امنیتی

- PCAP حاوی داده‌ی حساس است.

### ۱۱) جمع‌بندی مفهومی

- سه الگو.
- Evidence با شماره بسته.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) SYN بدون SYN-ACK؟ *(پاسخ: 28-5-ت1)*

**ت2.** (ساده) ICMP 3/4؟ *(پاسخ: 28-5-ت2)*

**ت3.** (متوسط) Retransmission بزرگ؟ *(پاسخ: 28-5-ت3)*

**ت4.** (متوسط) TLS alert certificate_unknown؟ *(پاسخ: 28-5-ت4)*

**ت5.** (سخت) Case 3 را رفع کنید. *(پاسخ: 28-5-ت5)*

**ت6.** (سخت، طراحی) قالب Evidence. *(پاسخ: 28-5-ت6)*

**Q1.** Quick quiz (English): Which wireshark filter finds retransmissions? *(پاسخ: 28-5-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| PCAP | Packet capture | فایل Capture |

- *Cite frame numbers as evidence.* ← شماره‌ی فریم‌ها را به‌عنوان Evidence ذکر کنید.

### ۱۴) کارت Lab

**کارت Lab:** آزمون PCAP (اجرا نشده). **Evidence:** `03-ops/pcap-rca.md`.

### ۱۵) منابع

- Wireshark User Guide
- RFC 1191

## پاسخ‌های فصل 28

> ابتدا بدون نگاه حل کنید. شناسه: درس-نوع+شماره (ت = تمرین، م = مرور).


### پاسخ‌های بازنویسی عمیق درس 28-1

**28-1-ت1** — تا مشخص شود بسته کجا ناپدید می‌شود: قبل یا بعد از فایروال.

**28-1-ت2** — هدر IP به‌علاوه‌ی نام Interface.

**28-1-ت3** — `tcp[tcpflags] & (tcp-syn|tcp-rst) != 0`.

**28-1-ت4** — بسته هم روی Interface ورودی و هم خروجی ثبت می‌شود.

**28-1-ت5** — Offload؛ Capture روی نقطه‌ی بیرونی یا غیرفعال موقت Offload در Window؛ تأیید.

**28-1-ت6** — مجوز، Filter حداقلی، زمان/حجم، رمزنگاری، Chain of custody، حذف.

**28-1-Q1** — To locate where the packet disappears relative to the firewall.


### پاسخ‌های بازنویسی عمیق درس 28-2

**28-2-ت1** — پورت مقصد بسته یا سرویس پاسخ‌گو نیست.

**28-2-ت2** — گیرنده بافر پر دارد و فرستنده باید متوقف شود؛ معمولاً مشکل برنامه است.

**28-2-ت3** — 64 KB/0.1 s ≈ 640 KB/s ≈ 5.2 Mbit/s.

**28-2-ت4** — 100 Mbit/s × 0.08 s = 8 Mbit = 1 MB.

**28-2-ت5** — ping DF اندازه‌ها برای MTU؛ Interface Errors/Loss برای لینک؛ MSS Clamp و رفع لینک؛ اندازه‌گیری مجدد.

**28-2-ت6** — سؤال، نقطه، Filter، الگوها، محاسبات، علت، رفع، تأیید.

**28-2-Q1** — Throughput is limited to the window size divided by the round-trip time.


### پاسخ‌های بازنویسی عمیق درس 28-3

**28-3-ت1** — نام سرور در ClientHello که معمولاً رمزنشده است.

**28-3-ت2** — چون پس از ServerHello رمز می‌شود.

**28-3-ت3** — کلاینت CA صادرکننده را نمی‌شناسد؛ معمولاً CA فایروال نصب نیست.

**28-3-ت4** — Issuer گواهی با `openssl s_client` از پشت فایروال برابر CA فایروال است.

**28-3-ت5** — Exemption آن مقصد؛ مستندسازی؛ آزمون منفی سایر مقصدها.

**28-3-ت6** — بلاک QUIC، پایش ECH، Exemption محدود، بازبینی.

**28-3-Q1** — openssl s_client combined with openssl x509 -noout -issuer.


### پاسخ‌های بازنویسی عمیق درس 28-4

**28-4-ت1** — چه تغییر کرد، چه کسی، از کی، لایه، رسیدن بسته، Route، Policy، NAT/Session، Profile، خروج/برگشت.

**28-4-ت2** — بار CPU و Log زیاد و خطر اطلاعات حساس.

**28-4-ت3** — احتمال×اثر÷هزینه‌ی آزمون؛ ارزان و محتمل اول.

**28-4-ت4** — Policy مقابل، Route برگشت، NAT-T/ESP، Selector؛ Debug Flow مقابل مشخص می‌کند.

**28-4-ت5** — شواهد مستقل برای هر علت، رفع یکی و اندازه‌گیری، سپس دیگری.

**28-4-ت6** — قالب یکسان، دسته‌بندی، جستجو، نسخه‌دار، بازبینی فصلی، پیوند به Runbook.

**28-4-Q1** — To find the cause faster by testing likely and cheap hypotheses first.


### پاسخ‌های بازنویسی عمیق درس 28-5


### پاسخ‌های بازنویسی عمیق درس 28-5

**28-5-ت1** — مقصد/مسیر پاسخ نمی‌دهد.

**28-5-ت2** — Fragmentation needed.

**28-5-ت3** — MTU/Loss.

**28-5-ت4** — گواهی ناشناخته.

**28-5-ت5** — CA یا Exempt.

**28-5-ت6** — frames، finding، fix، verify.

**28-5-Q1** — tcp.analysis.retransmission.

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

![شکل: چرخه‌ی پاسخ به حادثه.](../figures/ch29-l0-fig1.svg)

*شکل: چرخه‌ی پاسخ به حادثه.*

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

## درس 29-1 — Detection عملی: از Log فایروال به IOC/TTP، Baseline، آستانه، Correlation و Alert

**فصل 29 · بازنویسی عمیق · پیش‌نیاز: ۲۹-۰، ۲۷-۰، ۲۷-۱، ۲۸-۲ · ≈ 8 ساعت**

> **وضعیت:** مفهومی؛ فقط Lab ایزوله و مجاز؛ FortiOS 7.0.3 (بوت‌نشده)؛ دستورها `Unverified`؛ Lab «اجرا نشده».

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. از Log فایروال Detectionهای Scan، Brute-force، Exfiltration، حرکت جانبی و DNS مشکوک بسازد.
2. Baseline و آستانه (آماری و قاعده‌محور) را با FP/FN بسنجد.
3. Correlation چندمنبعی (Traffic+Event+DNS) را انجام دهد.
4. Alert را با Severity، Owner و Runbook مستند کند.
5. Detection را با سناریوی مجاز در Lab آزمایش و تنظیم کند.
6. Coverage را با ATT&CK مفهومی نگاشت کند.

### ۲) مفهوم پایه: چیست و چرا؟

Detection بدون Baseline پر از نویز است و بدون Correlation کور. هدف: Alertهای کم، دقیق و قابل‌اقدام. IOC (آدرس/Hash) زودگذر است؛ **رفتار (TTP)** پایدارتر است: اسکن، Brute-force، حرکت جانبی، خروج داده.

### ۳) توضیح عمیق فنی

#### ۱) Detection از Log

| رفتار | داده | منطق | آستانه‌ی اولیه |
|---|---|---|---|
| Port scan | Traffic: deny | یک srcip به N پورت/مقصد | > 100 پورت در ۲ دقیقه |
| Brute-force | Event: login failed | تعداد ناموفق | > 10 در ۵ دقیقه |
| ورود موفق پس از ناموفق | Event | ترکیب | ≥ 5 ناموفق سپس موفق |
| Exfiltration | Traffic: sentbyte | حجم خروجی | > Baseline + 3σ/روز |
| حرکت جانبی | Traffic: deny/allow بین Zone | دسترسی غیرعادی داخلی | هر Deny DMZ→DB |
| DNS مشکوک | DNS Log | دامنه‌ی نویزی/طول بلند/Rate بالا | Rate/entropy |

#### ۲) Baseline و آماری

``` text
Alert if x > mean + 3 x stddev   (per host or per hour of day)
FP rate = false alarms / alerts ; Precision = TP/(TP+FP)
```

الگوی زمانی (ساعت/روز کاری) را در Baseline لحاظ کنید.

#### ۳) Correlation

یک Alert قوی‌تر: «Deny مکرر از IP X» + «ورود موفق همان IP» + «حجم خروجی بالا». Join بر پایه‌ی `srcip`، `user`، زمان.

#### ۴) Alert حرفه‌ای

``` text
Name / Severity / Data source / Logic / Threshold / Owner / Runbook link / FP notes / Tuning date
```

#### ۵) آزمون در Lab

سناریوی مجاز: nmap محدود از Attacker-Lab؛ ۲۰ ورود ناموفق؛ انتقال فایل بزرگ؛ بررسی Alert و FP.

#### ۶) نگاشت ATT&CK

Scan→Discovery (TA0007)، Brute force→Credential Access (TA0006)، Lateral→Lateral Movement (TA0008)، Exfil→Exfiltration (TA0010).

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| آستانه | Baseline |
| Correlation | چندمنبعی |
| Exclusion | مستند+زمان‌دار |
| Runbook | برای هر Alert |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده):** Alert Scan: `srcip=198.51.100.7` Deny روی ۴۰۰ پورت در ۲ دقیقه؛ Block؛ بررسی Allow موفق (هیچ).

**متوسط (تحلیل):** Scanner داخلی مجاز FP می‌دهد: Exclusion بر پایه‌ی srcip و زمان؛ ثبت تاریخ بازبینی؛ نسبت FP از ۴۰٪ به ۵٪.

**سخت (Correlation):** ورود موفق VPN پس از ۱۲۰ ناموفق، سپس ۴۰۰ MB خروجی به IP ناشناس در ۱۰ دقیقه. Correlation سه رویداد ⇒ Severity بحرانی. اقدام: Contain، Scope، RCA. معیار: بدون Correlation سه Alert مجزا با اولویت پایین می‌ماند.

### ۷) پیاده‌سازی از مسیر CLI

``` text
execute log filter category 0
execute log filter field action deny
execute log filter field srcip 198.51.100.7
execute log display
```

### ۸) Verification (اثبات صحت)

- Alert آزمایشی (سناریوی مجاز).
- FP rate اندازه‌گیری.
- ماتریس ATT&CK.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| FP زیاد | Log | Exclusion/آستانه |
| FN | Coverage | Detection جدید |
| Alert نمی‌رسد | Syslog | مسیر |

### ۱۰) نکات امنیتی

- آزمون فقط Lab مجاز.
- Exclusion مستند.

### ۱۱) جمع‌بندی مفهومی

- رفتار بر IOC ارجحیت دارد.
- Baseline و آماری.
- Correlation.
- Alert با Owner/Runbook.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) IOC و TTP چه فرقی دارند؟ *(پاسخ: 29-1-ت1)*

**ت2.** (ساده) چرا Baseline لازم است؟ *(پاسخ: 29-1-ت2)*

**ت3.** (متوسط) آستانه‌ی mean+3σ یعنی چه؟ *(پاسخ: 29-1-ت3)*

**ت4.** (متوسط) چرا Exclusion باید زمان‌دار باشد؟ *(پاسخ: 29-1-ت4)*

**ت5.** (سخت) سه رویداد را Correlate و Severity بدهید. *(پاسخ: 29-1-ت5)*

**ت6.** (سخت، طراحی) ۵ Detection با داده/منطق/آستانه/Runbook. *(پاسخ: 29-1-ت6)*

**Q1.** Quick quiz (English): Why are behavior-based detections more durable than indicator-based ones? *(پاسخ: 29-1-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| TTP | Tactics, Techniques and Procedures | رفتار مهاجم |
| FP | False positive | هشدار کاذب |
| ATT&CK | MITRE ATT&CK | ماتریس تکنیک‌های مهاجم |

- *Know your baseline.* ← وضعیت عادی را بشناسید.

### ۱۴) کارت Lab

**کارت Lab:** Detection. **وضعیت:** اجرا نشده. **Evidence:** `03-ops/detect.md`.

### ۱۵) منابع

- NIST SP 800-61
- MITRE ATT&CK
- NIST SP 800-92

<a id="l-29-2"></a>

## درس 29-2 — Response و Playbook: مهار، Evidence، ریشه‌کنی، بازیابی و ارتباطات با مثال‌های اجرایی

**فصل 29 · بازنویسی عمیق · پیش‌نیاز: ۲۹-۰، ۲۹-۱، ۱۳-۷ · ≈ 8 ساعت**

> **وضعیت:** مفهومی؛ فقط Lab ایزوله و مجاز؛ FortiOS 7.0.3 (بوت‌نشده)؛ دستورها `Unverified`؛ Lab «اجرا نشده».

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. Playbook برای سه سناریو (Scan، Compromise سرور، حساب VPN لو رفته) بنویسد.
2. مهار با فایروال (Block، Quarantine، Session) را بدون تخریب Evidence اجرا کند.
3. ریشه‌کنی و بازیابی را با آزمون تأیید کند.
4. ارتباطات و Escalation را مستند کند.
5. تفاوت مهار کوتاه‌مدت/بلندمدت را بگوید.

### ۲) مفهوم پایه: چیست و چرا؟

در حادثه فشار زیاد است؛ Playbook یعنی از قبل تصمیم‌گیری. اشتباه رایج: مهار فوری که شواهد را پاک می‌کند، یا مهار ناقص که مهاجم را آگاه می‌کند.

### ۳) توضیح عمیق فنی

#### ۱) قالب Playbook

``` text
Trigger / Severity / Owner / Approvals
1 Triage: scope? asset? success? data?
2 Evidence preservation (what/where/how)
3 Containment: short-term, long-term
4 Eradication  5 Recovery + verification  6 Communication  7 Lessons learned
```

#### ۲) مهار با فایروال

- **Block IP:** Address + Deny Policy بالاتر از همه (Policy ID/موقت با تاریخ انقضا).
- **Quarantine:** قرنطینه‌ی میزبان (Policy/VLAN/Quarantine).
- **قطع Session:** `diagnose sys session clear` با Filter (۱۳-۷).
- **قطع VPN User:** غیرفعال کاربر + پایان Session.
- **Evidence پیش از مهار:** ذخیره‌ی Log/Session/Capture (مهار ممکن است Session را از بین ببرد).

#### ۳) سناریوها

**۱) Scan خارجی:** Block IP؛ بررسی Allowهای موفق؛ Hardening Local-in.
**۲) سرور DMZ Compromise:** ایزوله (Quarantine)، Evidence، بررسی مسیرها (Log DMZ→Internal)، بازسازی از Image، چرخش Credential.
**۳) حساب VPN لو رفته:** قفل حساب، پایان Session، بررسی دسترسی‌های کاربر، Reset+MFA، Detection تکراری.

#### ۴) بازیابی و تأیید

بازگشت به سرویس با Monitoring تشدیدشده، آزمون مثبت/منفی، حذف Ruleهای موقت، بازبینی Log ۷ روز.

#### ۵) ارتباطات

Timeline، اثر، وضعیت، اقدام بعدی، مسئول؛ ارتباط به مدیریت/حقوقی (در صورت نیاز)؛ ثبت.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| Block موقت | با انقضا و Owner |
| Evidence | قبل از مهار |
| Escalation | سطوح |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده):** Block IP اسکنر: Address `BLOCK-198.51.100.7` و Policy Deny بالا؛ تست: ping/nc از IP مسدود (Lab) رد؛ Log.

**متوسط (تحلیل):** Block اعمال شد ولی Session قبلی مهاجم فعال است: `session list` با Filter؛ Clear؛ تأیید قطع؛ درس: Block+Clear.

**سخت (Compromise سرور):** سرور DMZ با Webshell. Playbook: Evidence (Disk image/Log/Capture)، Quarantine، Scope (Traffic Log DMZ→Internal)، تعیین Credentialهای لمس‌شده، بازسازی، چرخش، Hardening (WAF/IPS)، PIR. اگر مهار قبل از Evidence انجام شود تحلیل ریشه ناقص می‌شود.

### ۷) پیاده‌سازی از مسیر CLI

``` text
config firewall address
    edit "BLOCK-198.51.100.7"
        set subnet 198.51.100.7 255.255.255.255
    next
end
diagnose sys session filter src 198.51.100.7
diagnose sys session list
diagnose sys session clear
diagnose sys session filter clear
```

### ۸) Verification (اثبات صحت)

- آزمون Block (Lab).
- Evidence ذخیره‌شده.
- PIR.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| Block بی‌اثر | ترتیب Policy | بالا ببرید |
| مهاجم برگشت | Credential | چرخش |

### ۱۰) نکات امنیتی

- Evidence اول؛ Rule موقت حذف شود.

### ۱۱) جمع‌بندی مفهومی

- Playbook قالب‌مند.
- Evidence پیش از مهار.
- Block+Clear.
- بازیابی با تأیید.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) چرا Evidence قبل از مهار؟ *(پاسخ: 29-2-ت1)*

**ت2.** (ساده) تفاوت مهار کوتاه‌مدت و بلندمدت؟ *(پاسخ: 29-2-ت2)*

**ت3.** (متوسط) Block شد ولی مهاجم هنوز متصل است؛ چرا؟ *(پاسخ: 29-2-ت3)*

**ت4.** (متوسط) پس از Compromise چه Credentialهایی چرخش یابند؟ *(پاسخ: 29-2-ت4)*

**ت5.** (سخت) Playbook Compromise سرور DMZ را ۷ مرحله‌ای بنویسید. *(پاسخ: 29-2-ت5)*

**ت6.** (سخت، طراحی) سه Playbook اولویت‌دار برای سازمان شما. *(پاسخ: 29-2-ت6)*

**Q1.** Quick quiz (English): Why combine blocking an IP with clearing its existing sessions? *(پاسخ: 29-2-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Quarantine | Host quarantine | قرنطینه‌ی میزبان |
| Scoping | Incident scoping | تعیین دامنه‌ی حادثه |

- *Preserve evidence before containment.* ← پیش از مهار Evidence را حفظ کنید.

### ۱۴) کارت Lab

**کارت Lab:** Response. **وضعیت:** اجرا نشده. **Evidence:** `03-ops/response.md`.

### ۱۵) منابع

- NIST SP 800-61 Rev.2
- SANS Incident Handler Handbook

<a id="l-29-3"></a>

## درس 29-3 — Lifecycle، Patch و Vulnerability Management: Inventory، EoL، PSIRT/CVE، اولویت‌بندی و Rollback

**فصل 29 · بازنویسی عمیق · پیش‌نیاز: ۲۷-۴، ۲۹-۰ · ≈ 8 ساعت**

> **وضعیت:** مفهومی؛ فقط Lab ایزوله و مجاز؛ FortiOS 7.0.3 (بوت‌نشده)؛ دستورها `Unverified`؛ Lab «اجرا نشده».

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. Inventory دارایی (مدل، نسخه، لایسنس، EoL) را نگه دارد.
2. CVE را با Exposure/Exploitability/Impact اولویت‌بندی کند.
3. Plan Patch با Lab، Window، Rollback و Verification بنویسد.
4. Compensating Controls را وقتی Patch ممکن نیست طراحی کند.
5. Metrics (Time-to-patch، Coverage) را اندازه بگیرد.

### ۲) مفهوم پایه: چیست و چرا؟

نسخه‌ی 7.0.3 قدیمی است و CVEهای شناخته‌شده دارد (مثل CVE-2022-40684، CVE-2022-42475، CVE-2023-27997 که در مستند پروژه ذکر شده‌اند). مدیریت آسیب‌پذیری یعنی «بدانید چه دارید، چه آسیب‌پذیر است، چه زمانی و چگونه امن می‌شود».

### ۳) توضیح عمیق فنی

#### ۱) Inventory

``` text
Device | Model | Serial | FortiOS | Role | Exposure(internet?) | License end | EoL/EoS | Owner
```

#### ۲) اولویت‌بندی

``` text
Priority ~= Severity(CVSS) x Exposure x Exploit availability x Asset criticality
```

مثال: CVE بحرانی روی SSL VPN اینترنتی با Exploit فعال ⇒ فوری (۲۴ تا ۷۲ ساعت). CVE روی سرویس داخلی غیرقابل‌دسترس ⇒ برنامه‌ریزی‌شده.

#### ۳) چرخه

PSIRT/CVE Feed → ارزیابی تأثیر روی نسخه/ویژگی → تصمیم (Patch/Workaround/Accept) → Lab → Window → Rollback آماده → Verification → ثبت.

#### ۴) Compensating Controls

وقتی Patch فوراً ممکن نیست: محدودسازی Source، غیرفعال‌کردن ویژگی (SSL VPN)، IPS Signature، Segmentation، پایش اضافه، WAF/Reverse proxy.

#### ۵) EoL/EoS

برنامه‌ی ارتقا قبل از پایان پشتیبانی؛ نسخه‌ی هدف و مسیر ارتقا (Upgrade Path) را از مستند Fortinet بگیرید.

#### ۶) Metrics

``` text
Time-to-patch (critical) = patch date - advisory date
Coverage = patched devices / total devices
```

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| اولویت | Exposure×Exploit×Criticality |
| Compensating | وقتی Patch نیست |
| Canary | برای ناوگان بزرگ |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده):** جدول Inventory ۳ دستگاه؛ نسخه‌ها؛ فهرست CVE مرتبط؛ اولویت.

**متوسط (تحلیل):** CVE بحرانی SSL VPN و دستگاه اینترنتی: فوری. اقدام: Lab Patch، Window، Backup، Rollback؛ اگر ۷۲ ساعت ممکن نبود: غیرفعال SSL VPN/Source Restriction موقت.

**سخت (طراحی):** ۲۰ دستگاه، ۲ شب Window در ماه، Upgrade Path چندمرحله‌ای. طرح: دسته‌بندی بر اساس Exposure؛ اینترنتی‌ها اول؛ Canary؛ HA یکی‌یکی؛ Verification و Rollback؛ Time-to-patch هدف ۷ روز برای بحرانی.

### ۷) پیاده‌سازی از مسیر CLI

``` text
get system status
execute backup config sftp pre-patch.conf 192.168.90.10 backup-user <PASSWORD>
```

### ۸) Verification (اثبات صحت)

- Inventory کامل.
- Plan Patch.
- Metrics ثبت.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| Patch شکست | Pre/Post-check | Rollback |
| ناسازگاری ویژگی | Release notes | برنامه |

### ۱۰) نکات امنیتی

- Patch سریع برای اینترنتی؛ Backup قبل.

### ۱۱) جمع‌بندی مفهومی

- Inventory→ارزیابی→Patch→Rollback.
- اولویت ریسک‌محور.
- Compensating Controls.
- Metrics.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) EoL یعنی چه؟ *(پاسخ: 29-3-ت1)*

**ت2.** (ساده) چرا Exposure در اولویت وزن بالا دارد؟ *(پاسخ: 29-3-ت2)*

**ت3.** (متوسط) Patch ممکن نیست؛ چه می‌کنید؟ *(پاسخ: 29-3-ت3)*

**ت4.** (متوسط) Time-to-patch چیست؟ *(پاسخ: 29-3-ت4)*

**ت5.** (سخت) طرح Patch ۲۰ دستگاه با ۲ Window ماهانه. *(پاسخ: 29-3-ت5)*

**ت6.** (سخت، طراحی) داشبورد Metrics آسیب‌پذیری. *(پاسخ: 29-3-ت6)*

**Q1.** Quick quiz (English): Which factors raise the urgency of patching a vulnerability? *(پاسخ: 29-3-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| PSIRT | Product Security Incident Response Team | تیم امنیت محصول |
| CVSS | Common Vulnerability Scoring System | سامانه‌ی امتیاز آسیب‌پذیری |
| EoL | End of Life | پایان عمر |

- *Track end-of-life dates and plan upgrades early.* ← تاریخ پایان عمر را پیگیری و ارتقا را زود برنامه‌ریزی کنید.

### ۱۴) کارت Lab

**کارت Lab:** Patch. **وضعیت:** اجرا نشده. **Evidence:** `03-ops/patch.md`.

### ۱۵) منابع

- FortiGuard PSIRT
- NIST SP 800-40 Rev.4
- FIRST CVSS

<a id="l-29-4"></a>

## درس 29-4 — گزارش حادثه (PIR) و آزمون عملی Blue Team: سناریوی چندمرحله‌ای با کلید و Rubric

**فصل 29 · بازنویسی عمیق · پیش‌نیاز: ۲۹-۱ تا ۲۹-۳ · ≈ 12 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ سناریو و کلید پاسخ آموزشی‌اند؛ Lab «اجرا نشده»؛ دستورها `Unverified` تا اجرای Lab؛ ویژگی‌های وابسته به لایسنس مشخص شده‌اند.

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. یک حادثه‌ی چندمرحله‌ای (Brute-force → دسترسی → حرکت جانبی) را از Log بازسازی کند.
2. Timeline، Containment، Eradication و Recovery را بنویسد.
3. MTTD/MTTR را محاسبه کند.
4. PIR بی‌ملامت (Blameless) با اقدام پیشگیرانه بنویسد.
5. آزمون را با Rubric تحویل دهد.

### ۲) مفهوم پایه: چیست و چرا؟

حادثه‌ی واقعی هیچ‌وقت با برچسب «حمله‌ی چندمرحله‌ای» نمی‌آید. چند هشدار پراکنده می‌آید و مهندس باید آن‌ها را به یک داستان وصل کند. PIR (Post-Incident Review) آموختن از آن داستان است، نه تقصیر.

### ۳) توضیح عمیق فنی

#### ۱) سناریو

ساعت 02:10 Alert: ۴۰ ورود ناموفق SSH به FGT از IP 192.0.2.77. 02:14 ورود موفق admin. 02:20 تغییر Policy و ایجاد حساب `svc-tmp`. 02:35 اتصال از FGT به 10.20.0.10:445 (Scan). 03:05 SOC متوجه می‌شود.

#### ۲) Timeline

| ساعت | رویداد | منبع |
|---|---|---|
| 02:10 | Brute-force SSH | Event log |
| 02:14 | ورود موفق | Event log |
| 02:20 | ساخت `svc-tmp` | Config change log |
| 02:35 | Scan داخلی | Forward traffic |
| 03:05 | کشف | SOC |

MTTD = 03:05 − 02:10 = 55 دقیقه.

#### ۳) پاسخ

**Containment:** Block IP با Local-in، غیرفعال کردن admin و `svc-tmp`، جدا کردن Mgmt، کنسول. **Eradication:** حذف حساب‌ها، تغییر رمزها/کلیدها، بررسی Config Diff با Backup، پچ. **Recovery:** Restore Config پاک، Monitoring تشدید.

#### ۴) ریشه

SSH روی WAN باز و بدون MFA/Trusted host؛ رمز ضعیف.

#### ۵) اقدام پیشگیرانه

حذف SSH از WAN، MFA، Trusted host، Alert بر Brute-force، بازبینی Config روزانه (Diff)، آموزش.

#### ۶) PIR (قالب)

``` text
Summary / Impact / Timeline / Root cause / What went well / What failed / Actions (owner, due) / Lessons
```

#### ۷) Rubric

Timeline ۲۰، Containment/Eradication ۲۰، ریشه ۲۰، اقدام ۲۰، PIR و MTTD/MTTR ۱۵، صداقت ۵. قبولی ۷۵.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| Containment | اول جلوگیری |
| PIR | Blameless |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده):** MTTD = 03:05 − 02:10 = ۵۵ دقیقه؛ MTTR (تا Containment 03:25) = ۷۵ دقیقه از شروع.

**متوسط (Containment):** اول IP مهاجم را Block و Admin/svc-tmp را غیرفعال؛ سپس Config را با Backup مقایسه؛ برای جلوگیری از حذف شواهد Log را ذخیره.

**سخت (PIR):** نوشتن PIR کامل: خلاصه، اثر (دسترسی به Config، Scan داخلی بدون نفوذ به سرور)، Timeline، ریشه (SSH WAN + رمز ضعیف)، موفق (Alert دریافت شد)، شکست (۵۵ دقیقه تأخیر)، اقدام‌ها با مالک و تاریخ.

### ۷) پیاده‌سازی از مسیر CLI

``` text
execute log filter category 1
execute log display
```

### ۸) Verification (اثبات صحت)

- Timeline با Log.
- اقدام‌ها مالک دارند.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| Timeline ناقص | Log | NTP/Log متمرکز |

### ۱۰) نکات امنیتی

- شواهد را حفظ کنید.

### ۱۱) جمع‌بندی مفهومی

- از Alert به داستان.
- Containment.
- Blameless PIR.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) MTTD چیست؟ *(پاسخ: 29-4-ت1)*

**ت2.** (ساده) Containment؟ *(پاسخ: 29-4-ت2)*

**ت3.** (متوسط) اولین اقدام؟ *(پاسخ: 29-4-ت3)*

**ت4.** (متوسط) ریشه؟ *(پاسخ: 29-4-ت4)*

**ت5.** (سخت) PIR بنویسید. *(پاسخ: 29-4-ت5)*

**ت6.** (سخت، طراحی) اقدام پیشگیرانه. *(پاسخ: 29-4-ت6)*

**Q1.** Quick quiz (English): What does MTTD measure? *(پاسخ: 29-4-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| PIR | Post-Incident Review | بازبینی پس از حادثه |
| MTTD | Mean Time To Detect | میانگین زمان کشف |

- *A blameless review focuses on process, not people.* ← بازبینی بی‌ملامت روی فرایند است نه افراد.

### ۱۴) کارت Lab

**کارت Lab:** آزمون Blue Team (اجرا نشده). **Evidence:** `03-ops/pir-29.md`.

### ۱۵) منابع

- NIST SP 800-61 Rev.2

## پاسخ‌های فصل 29

> ابتدا بدون نگاه حل کنید. شناسه: درس-نوع+شماره (ت = تمرین، م = مرور).


### پاسخ‌های بازنویسی عمیق درس 29-1

**29-1-ت1** — IOC نشانه‌ی مشخص و زودگذر (IP/Hash)؛ TTP رفتار و روش مهاجم و پایدارتر.

**29-1-ت2** — تا انحراف از رفتار عادی تشخیص داده شود و FP کم شود.

**29-1-ت3** — مقداری بیش از میانگین به‌علاوه‌ی سه برابر انحراف معیار Alert می‌دهد (تقریباً رویداد نادر).

**29-1-ت4** — تا استثنا فراموش و به حفره تبدیل نشود؛ بازبینی دوره‌ای.

**29-1-ت5** — ناموفق مکرر + ورود موفق + خروجی بالا ⇒ احتمال نفوذ؛ Severity بحرانی؛ Contain/Scope/RCA.

**29-1-ت6** — جدول بالا بسط داده شود.

**29-1-Q1** — Because attackers can change IPs and hashes easily but their behaviors change much less.


### پاسخ‌های بازنویسی عمیق درس 29-2

**29-2-ت1** — مهار ممکن است Session/حافظه/Log را تغییر دهد و تحلیل را ناقص کند.

**29-2-ت2** — کوتاه‌مدت جلوگیری فوری (Block/Quarantine)؛ بلندمدت رفع ریشه‌ای (بازسازی/Patch/چرخش).

**29-2-ت3** — Session قبلی باقی است؛ باید Clear فیلترشده انجام شود.

**29-2-ت4** — حساب‌های موجود روی سرور، سرویس‌ها، Tokenها و Credentialهایی که سرور به آن‌ها دسترسی داشت.

**29-2-ت5** — Triage، Evidence، Quarantine، Scope، Eradicate/Rebuild، Recover/Verify، PIR با Owner/زمان.

**29-2-ت6** — Scan/Brute-force، سرور Compromise، حساب لو رفته؛ هرکدام Trigger/Approvals/دستور.

**29-2-Q1** — Because a block applies to new connections while existing sessions may continue.


### پاسخ‌های بازنویسی عمیق درس 29-3

**29-3-ت1** — پایان پشتیبانی و Patch امنیتی محصول.

**29-3-ت2** — آسیب‌پذیری قابل‌دسترس از اینترنت سریع‌تر و گسترده‌تر سوءاستفاده می‌شود.

**29-3-ت3** — Compensating Controls: Source Restriction، غیرفعال ویژگی، IPS، Segmentation، پایش.

**29-3-ت4** — فاصله‌ی انتشار Advisory تا اعمال Patch.

**29-3-ت5** — اولویت بر Exposure، Canary، HA یکی‌یکی، Backup/Rollback، Verification، هدف Time-to-patch.

**29-3-ت6** — Coverage، Time-to-patch، تعداد EoL، Exception فعال، Trend.

**29-3-Q1** — Internet exposure, available exploits and high asset criticality.


### پاسخ‌های بازنویسی عمیق درس 29-4


### پاسخ‌های بازنویسی عمیق درس 29-4

**29-4-ت1** — زمان تا کشف.

**29-4-ت2** — جلوگیری از گسترش.

**29-4-ت3** — Block و غیرفعال حساب.

**29-4-ت4** — SSH WAN و رمز.

**29-4-ت5** — قالب.

**29-4-ت6** — حذف SSH WAN، MFA، Alert.

**29-4-Q1** — The mean time between the start of an incident and its detection.

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

## درس 30-1 — Migration: Inventory، Rule Hygiene و نگاشت دقیق Object/NAT/Policy/VPN به FortiGate

**فصل 30 · بازنویسی عمیق · پیش‌نیاز: ۳۰-۰، ۲۵-۱، ۱۳-۱ · ≈ 8 ساعت**

> **وضعیت:** روش‌شناسی مستقل از برند؛ نگاشت ASA→FortiGate مفهومی/`Unverified`؛ فقط Lab/Change مجاز؛ FortiOS 7.0.3 (بوت‌نشده).

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. Inventory کامل از دستگاه مبدأ (Interface، Route، NAT، ACL، VPN، User، Log) تهیه کند.
2. Rule Hygiene (Hit Count، Shadow، Duplicate، Any-Any) را انجام دهد.
3. نگاشت مفهومی Object/Service/ACL/NAT/VPN به FortiGate را بنویسد و تفاوت مدل را تحلیل کند.
4. ریسک‌های رفتاری (ترتیب NAT/ACL، Implicit rules، Inspection) را فهرست کند.
5. Mapping Table و Gap List بسازد.
6. نیازمندی‌های ابزار خودکار (FortiConverter) و محدودیت‌ها را بداند.

### ۲) مفهوم پایه: چیست و چرا؟

مهاجرت موفق یعنی **برابری رفتاری**، نه برابری متن Config. «کپی» خطرناک است چون مدل پردازش فرق دارد: در ASA سطح امنیت و ACL و NAT ترتیب خاص دارند؛ در FortiGate Policy و Session و NAT در Policy/Central NAT. پیش‌شرط: بدانید دقیقاً چه دارید.

### ۳) توضیح عمیق فنی

#### ۱) Inventory (منابع)

``` text
show running-config            show access-list (hit counts) show nat detail
show route                     show vpn-sessiondb / crypto maps
show conn count                show xlate count    logs (90 days)
user/group, certificates, DHCP/DNS/AAA, routing protocols, SNMP/NTP/Syslog
```

#### ۲) Rule Hygiene

| مورد | تشخیص | اقدام |
|---|---|---|
| Rule بدون Hit (90 روز) | Hit count = 0 | حذف/بایگانی |
| Shadow | Rule بالاتر همه را می‌گیرد | حذف |
| Duplicate/Overlap | Object/Rule هم‌پوشان | ادغام |
| Any-Any | مبدأ/مقصد/سرویس any | محدودسازی |
| Object بی‌استفاده | بدون مرجع | حذف |

#### ۳) نگاشت مفهومی

| مبدأ (ASA) | FortiGate |
|---|---|
| nameif + security-level | Interface/Zone + Policy صریح (Implicit deny) |
| object network/service/group | Address/Service/Group |
| access-list + access-group | Firewall Policy (srcintf/dstintf) |
| NAT (object/twice) | Policy NAT/VIP/IP Pool/Central NAT |
| route/dynamic routing | Static/OSPF/BGP |
| crypto map/tunnel-group | IPsec Phase1/2 Route-based |
| MPF inspect | Session Helper/ALG/Profile |
| AAA/LDAP | User/LDAP/RADIUS |

#### ۴) تفاوت‌های رفتاری حیاتی

- **Implicit rules:** ASA ترافیک از امنیت بالا به پایین را پیش‌فرض اجازه می‌دهد؛ FortiGate هیچ‌چیز (Implicit deny).
- **ترتیب NAT:** ASA NAT را پیش از ACL (با Real IP در ACL پس از 8.3)؛ FortiGate DNAT قبل از Policy و SNAT بعد.
- **Interface:** `nameif` به Zone/Interface؛ چند Interface یک Zone.
- **Inspection:** پیش‌فرض‌ها متفاوت (ALG).

#### ۵) Mapping Table

``` text
Source object -> Target object | Rule ID -> Policy ID | NAT entry -> Policy/VIP | Gap | Test case
```

#### ۶) ابزار خودکار

FortiConverter (لایسنس/سرویس) Config را تبدیل می‌کند ولی **خروجی باید بازبینی و آزمون شود** (`Unverified` برای قابلیت‌ها).

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| ابزار خودکار یا دستی | Hygiene دستی + ابزار برای حجم؛ بازبینی اجباری |
| Zone | نگاشت security-level به Zone |
| Implicit rules | صریح‌سازی |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده):** ۲۴۰ Rule: ۱۱۰ صفر-Hit حذف؛ ۱۳۰ باقی؛ Mapping Table ۱۳۰ سطری.

**متوسط (تحلیل):** در ASA ترافیک Inside→DMZ بدون Rule مجاز بود (security-level)؛ در FGT بدون Policy Block می‌شود. نتیجه: «قطع پس از Cutover». پیشگیری: استخراج رفتار ضمنی به Policy صریح و آزمون.

**سخت (NAT):** Twice-NAT با ترتیب خاص و Object با Real/Mapped Address. نگاشت به FGT: VIP + Policy با مقصد post-DNAT + IP Pool؛ خطای رایج: Policy با IP عمومی به‌جای داخلی. آزمون: Debug Flow و Test Matrix. ریسک: Hairpin NAT و ALG.

### ۸) Verification (اثبات صحت)

- Mapping Table کامل و Gap List.
- Hit Count ۹۰ روز.
- Test Cases قبل از Build.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| Rule ناشناخته | Hit/Log | Owner |
| NAT نگاشت نمی‌شود | Test | VIP/Pool |
| Implicit rule | تست | Policy صریح |

### ۱۰) نکات امنیتی

- Secret/رمز منتقل نشود.
- Any-Any را منتقل نکنید.

### ۱۱) جمع‌بندی مفهومی

- برابری رفتاری هدف است.
- Hygiene قبل از نگاشت.
- Implicit rules را صریح کنید.
- Mapping/Gap Table.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) Hit Count چیست؟ *(پاسخ: 30-1-ت1)*

**ت2.** (ساده) چرا Hygiene قبل از مهاجرت؟ *(پاسخ: 30-1-ت2)*

**ت3.** (متوسط) تفاوت Implicit در ASA و FortiGate؟ *(پاسخ: 30-1-ت3)*

**ت4.** (متوسط) Policy VIP باید مقصد را چه بگذارد؟ *(پاسخ: 30-1-ت4)*

**ت5.** (سخت) Twice-NAT را به FGT نگاشت کنید. *(پاسخ: 30-1-ت5)*

**ت6.** (سخت، طراحی) Mapping Table و Gap List برای ۱۰ Rule نمونه. *(پاسخ: 30-1-ت6)*

**Q1.** Quick quiz (English): Why is behavioral equivalence the goal rather than configuration equivalence? *(پاسخ: 30-1-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Hit count | Rule hit count | تعداد Match |
| Shadowed rule | Shadowed rule | Rule پنهان‌شده |
| security-level | ASA security level | سطح امنیت ASA |

- *Remove dead rules before migrating.* ← قبل از مهاجرت Ruleهای مرده را حذف کنید.

### ۱۴) کارت Lab

**کارت Lab:** Inventory/Mapping. **وضعیت:** اجرا نشده. **Evidence:** `02-design/mig-inventory.md`.

### ۱۵) منابع

- NIST SP 800-41
- Fortinet FortiConverter documentation
- Cisco ASA 9.x NAT reference

<a id="l-30-2"></a>

## درس 30-2 — Plan، Cutover و Rollback: برنامه‌ی تغییر، معیار Go/No-Go، Trigger و ارتباطات

**فصل 30 · بازنویسی عمیق · پیش‌نیاز: ۳۰-۰، ۳۰-۱، ۳۲-۰ · ≈ 8 ساعت**

> **وضعیت:** روش‌شناسی مستقل از برند؛ نگاشت ASA→FortiGate مفهومی/`Unverified`؛ فقط Lab/Change مجاز؛ FortiOS 7.0.3 (بوت‌نشده).

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. Plan Cutover ده‌مرحله‌ای را با زمان‌بندی دقیقه‌ای بنویسد.
2. معیار Go/No-Go و Rollback Trigger را تعریف کند.
3. Pre-check/Post-check و آزمون مثبت/منفی را بنویسد.
4. ارتباطات و Escalation را برنامه‌ریزی کند.
5. Cutover را در Lab اجرا و Rollback را آزمایش کند.

### ۲) مفهوم پایه: چیست و چرا؟

Cutover لحظه‌ی خطر است. Plan باید طوری باشد که یک مهندس دیگر هم بتواند اجرا کند؛ و تصمیم Rollback پیش از شروع مشخص باشد تا زیر فشار تصمیم احساسی نگیرید.

### ۳) توضیح عمیق فنی

#### ۱) اجزای Plan

``` text
Scope / Window / Team roles (executor, verifier, comms, approver)
Pre-checks: backups both, access (OOB), license, firmware, test matrix ready
Go/No-Go checklist (T-60 min)
Steps with timing: T+0 ... (each step: action, expected result, verification)
Post-checks: test matrix, Log/Session, monitoring
Rollback: trigger criteria, steps, time to complete
Communication: start, milestones, completion, escalation
```

#### ۲) Go/No-Go

همه‌ی Pre-checkها OK؛ OOB کار می‌کند؛ Backup تأیید؛ تیم کامل؛ شرایط (بدون Freeze). یک «No» ⇒ لغو.

#### ۳) Rollback Trigger (نمونه)

- سرویس حیاتی X پس از ۳۰ دقیقه برنگشت.
- ≥ ۲ آزمون مثبت حیاتی شکست.
- مشکل ناشناخته‌ی امنیتی.
Rollback باید زمان‌بندی داشته باشد (مثلاً ۱۵ دقیقه) و در Lab آزمایش شده باشد.

#### ۴) مراحل نمونه

``` text
T-60 Go/No-Go     T-30 final backups     T+0 announce
T+5 move gateway/route to new FGT        T+10 pre-defined smoke tests
T+20 full test matrix                    T+35 decision: continue / rollback
T+45 monitor + comms                     T+60 close window or hypercare
```

#### ۵) Hypercare

۷ تا ۱۴ روز پایش تشدیدشده؛ Log؛ تماس سریع؛ نگه‌داشتن دستگاه قدیمی آماده تا N روز.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| Window | کم‌ترافیک |
| Trigger | پیش‌تعریف |
| OOB | اجباری |
| Hypercare | ۷–۱۴ روز |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده):** Plan یک‌صفحه‌ای با ۱۰ مرحله و Rollback.

**متوسط (تحلیل):** در T+20 فقط ۲ از ۱۰ آزمون شکست می‌خورد: تصمیم بر پایه‌ی Trigger: اگر سرویس حیاتی نیست ادامه با رفع؛ اگر حیاتی ⇒ Rollback. ثبت تصمیم و دلیل.

**سخت (ریسک):** Cutover ساعت ۲ بامداد؛ دسترسی OOB قطع می‌شود. شواهد: ممنوعیت Cutover بدون OOB. طرح: Console Server/مسیر دوم؛ Go/No-Go شامل تست OOB. اگر مشکل پس از شروع: Rollback با دسترسی فیزیکی. درس: Pre-check OOB اجباری.

### ۷) پیاده‌سازی از مسیر CLI

``` text
execute backup config sftp pre-cutover.conf 192.168.90.10 backup-user <PASSWORD>
get system status
```

### ۸) Verification (اثبات صحت)

- Plan بازبینی‌شده.
- Rollback آزمایش‌شده در Lab.
- Go/No-Go امضا.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| Cutover شکست | Post-check | Rollback |
| OOB نیست | تست | لغو |

### ۱۰) نکات امنیتی

- Change رسمی و Rollback.

### ۱۱) جمع‌بندی مفهومی

- Plan + Go/No-Go + Trigger + Rollback.
- OOB و Backup الزامی.
- Hypercare.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) Go/No-Go چیست؟ *(پاسخ: 30-2-ت1)*

**ت2.** (ساده) Rollback Trigger چیست؟ *(پاسخ: 30-2-ت2)*

**ت3.** (متوسط) چرا OOB لازم است؟ *(پاسخ: 30-2-ت3)*

**ت4.** (متوسط) چه چیزی در Post-check؟ *(پاسخ: 30-2-ت4)*

**ت5.** (سخت) ۲ آزمون از ۱۰ شکست خورد؛ تصمیم و ثبت. *(پاسخ: 30-2-ت5)*

**ت6.** (سخت، طراحی) Plan ده‌مرحله‌ای برای Cutover فایروال لبه. *(پاسخ: 30-2-ت6)*

**Q1.** Quick quiz (English): Why must rollback criteria be defined before the change? *(پاسخ: 30-2-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| OOB | Out-of-band management | مدیریت خارج از مسیر داده |
| Hypercare | Hypercare | پایش ویژه پس از تغییر |

- *Always have a tested rollback plan.* ← همیشه Rollback Plan آزمون‌شده داشته باشید.

### ۱۴) کارت Lab

**کارت Lab:** Plan. **وضعیت:** اجرا نشده. **Evidence:** `02-design/mig-plan.md`.

### ۱۵) منابع

- ITIL 4 Change Enablement
- Google SRE Book (Release engineering)

<a id="l-30-3"></a>

## درس 30-3 — تست پیش/پس Migration و Evidence: Test Matrix، مقایسه‌ی Session/Log، RCA اختلاف‌ها

**فصل 30 · بازنویسی عمیق · پیش‌نیاز: ۳۰-۱، ۳۰-۲ · ≈ 11 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ سناریو و کلید آموزشی؛ Lab «اجرا نشده»؛ دستورها `Unverified` تا اجرای Lab؛ FMG/FAZ وابسته به لایسنس (Needs-License).

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. Test Matrix پیش و پس را با معیار عددی بنویسد.
2. Session، Route، Policy hit و Log را قبل/بعد مقایسه کند.
3. اختلاف‌ها را دسته‌بندی (قابل‌قبول/نیازمند رفع) و RCA کند.
4. Evidence را سازمان‌دهی کند.
5. تصمیم Go/No-Go بگیرد.

### ۲) مفهوم پایه: چیست و چرا؟

پس از Migration می‌پرسند «همه‌چیز مثل قبل است؟». بدون Baseline نمی‌توانید جواب دهید. این درس نشان می‌دهد چه چیزهایی را قبل از تغییر اندازه بگیرید تا پس از آن با عدد جواب دهید.

### ۳) توضیح عمیق فنی

#### ۱) Baseline

``` text
get system status
diagnose sys session stat
get router info routing-table all
diagnose firewall iprope list (summary)   Unverified
policy hit counts (top 20)
IPsec: get vpn ipsec tunnel summary
```

#### ۲) Test Matrix

| # | آزمون | قبل | بعد | معیار |
|---|---|---|---|---|
| 1 | ping/DNS | ok | ok | برابر |
| 2 | HTTPS خروج | ok | ok | برابر |
| 3 | VIP وب | ok | ok | برابر |
| 4 | IPsec | up | up | برابر |
| 5 | تعداد Session | 41k | 39k | ±10٪ |
| 6 | Routeها | N | N | برابر |
| 7 | Policy hit | baseline | مقایسه | روند مشابه |
| 8 | Log | ok | ok | ورود Log |

#### ۳) دسته‌بندی اختلاف

| اختلاف | دسته | اقدام |
|---|---|---|
| Session 5٪ کمتر | قابل‌قبول | ثبت |
| IPsec down | بحرانی | RCA و رفع |
| Policy hit صفر | بررسی | Mapping |

#### ۴) RCA نمونه

IPsec down: Proposal پیش‌فرض نسخه‌ی جدید تغییر کرده؛ شاهد Debug؛ رفع صریح؛ پیشگیری: Config صریح (نه اتکا به پیش‌فرض).

#### ۵) Go/No-Go

Go اگر همه‌ی بحرانی‌ها OK و اختلاف قابل‌قبول؛ No-Go ⇒ Rollback.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| Baseline | قبل از تغییر |
| Go/No-Go | معیار عددی |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده):** Session قبل 41k، بعد 39k ⇒ −۴٫۹٪ ⇒ قابل‌قبول.

**متوسط (Policy hit):** Policy 20 قبل Hit 1M، بعد 0. علت: Interface Mapping اشتباه (port2 ↔ port3). رفع: Mapping؛ Hit بازگشت.

**سخت (Go/No-Go):** IPsec up ولی دانلود می‌ایستد، Log ingestion قطع. تصمیم: No-Go؛ Rollback ظرف ۱۰ دقیقه؛ RCA در Lab (MTU/Log setting)؛ اقدام: آزمون کامل پیش از تلاش دوم.

### ۷) پیاده‌سازی از مسیر CLI

``` text
diagnose sys session stat
get vpn ipsec tunnel summary
```

### ۸) Verification (اثبات صحت)

- Test Matrix.
- Evidence.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| Session کم | Timeout | session-ttl |

### ۱۰) نکات امنیتی

- Evidence بدون رمز.

### ۱۱) جمع‌بندی مفهومی

- Baseline.
- Matrix.
- RCA.
- Go/No-Go.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) چرا Baseline؟ *(پاسخ: 30-3-ت1)*

**ت2.** (ساده) ±۱۰٪؟ *(پاسخ: 30-3-ت2)*

**ت3.** (متوسط) Policy hit صفر؟ *(پاسخ: 30-3-ت3)*

**ت4.** (متوسط) دسته‌بندی؟ *(پاسخ: 30-3-ت4)*

**ت5.** (سخت) No-Go چه می‌کنید؟ *(پاسخ: 30-3-ت5)*

**ت6.** (سخت، طراحی) Test Matrix. *(پاسخ: 30-3-ت6)*

**Q1.** Quick quiz (English): Why must you collect a baseline before migration? *(پاسخ: 30-3-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Baseline | Baseline measurement | اندازه‌ی مبنا |

- *Compare before and after with evidence.* ← قبل و بعد را با شواهد مقایسه کنید.

### ۱۴) کارت Lab

**کارت Lab:** تست Migration (اجرا نشده). **Evidence:** `03-ops/migration-tests.md`.

### ۱۵) منابع

- Fortinet FortiOS 7.0 Administration Guide: Upgrade

<a id="l-30-4"></a>

## درس 30-4 — Gate G11: آزمون عملی Migration — صورت مسئله، کلید پاسخ کامل و Rubric

**فصل 30 · بازنویسی عمیق · پیش‌نیاز: ۳۰-۱ تا ۳۰-۳ · ≈ 12 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ سناریو و کلید پاسخ آموزشی‌اند؛ Lab «اجرا نشده»؛ دستورها `Unverified` تا اجرای Lab؛ ویژگی‌های وابسته به لایسنس مشخص شده‌اند.

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. برنامه‌ی Migration (Plan، Pre-check، Cutover، Post-check، Rollback) را بنویسد.
2. Test Matrix پیش/پس را اجرا و مقایسه کند.
3. اختلاف‌ها را با RCA تحلیل کند.
4. Rollback را در Lab آزمون کند.
5. گزارش و Rubric را تحویل دهد.

### ۲) مفهوم پایه: چیست و چرا؟

Migration یعنی تعویض فایروال قدیمی با جدید بدون قطع طولانی. خطر اصلی «کار می‌کرد، حالا نه» است؛ پس باید از قبل بدانید چه چیزی کار می‌کرد (Baseline) و پس از آن همان را اندازه بگیرید. این Gate سنجش همین انضباط است.

### ۳) توضیح عمیق فنی

#### ۱) صورت مسئله

جایگزینی FGT-OLD (v6.4) با FGT-NEW (v7.0.3) در Lab. نیاز: Config تبدیل‌شده، Policyها هم‌ارز، Cutover در Window ۶۰ دقیقه‌ای، Rollback زیر ۱۰ دقیقه.

#### ۲) Plan

``` text
T-7d  inventory, baseline, backup
T-3d  convert config, review diff, lab test
T-1d  dry run in Lab, rollback test
T0    cutover (change window 60 min)
T+1h  post-check
T+1d  monitoring review, close CHG
```

#### ۳) Test Matrix

| # | آزمون | قبل | بعد |
|---|---|---|---|
| 1 | ping GW و DNS | ok | ok |
| 2 | HTTPS خروج | ok | ok |
| 3 | VIP وب | ok | ok |
| 4 | IPsec Site-to-Site | up | up |
| 5 | Session count | N | ≈N |
| 6 | Policy hit counts | baseline | مقایسه |
| 7 | Log ingestion | ok | ok |

#### ۴) Cutover و Rollback

``` text
1 backup OLD and NEW
2 move cables or VIP in documented order
3 run test matrix (items 1-7)
4 if any critical fail within 15 min -> rollback: restore cabling/IP, verify OLD
```

#### ۵) مقایسه‌ی اختلاف‌ها

- Session count بعد ۱۰٪ کمتر: Timeout یا offload متفاوت؛ بررسی `get system session-ttl`.
- IPsec up نمی‌شود: Proposal پیش‌فرض نسخه‌ی جدید عوض شده؛ مقایسه با Release Notes.
- Policy hit صفر: ترتیب/Interface نگاشت اشتباه.

#### ۶) Rubric

Plan ۲۰، Test Matrix ۲۵، Cutover/Rollback ۲۰، اختلاف‌ها و RCA ۲۰، Evidence و صداقت ۱۵. قبولی ۷۵.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| Window | ۶۰ دقیقه با Rollback |
| Baseline | قبل از تغییر |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده):** Test Matrix ردیف ۱–۳ قبل از Cutover ok؛ بعد ok؛ ثبت زمان و خروجی.

**متوسط (اختلاف):** IPsec پس از Cutover down. مراحل: ۱) Debug IKE: NO_PROPOSAL. ۲) نسخه‌ی جدید Proposal پیش‌فرض متفاوت. ۳) تنظیم صریح Proposal. ۴) up. RCA: وابستگی به پیش‌فرض نسخه.

**سخت (Rollback):** ۱۵ دقیقه پس از Cutover VIP وب کار نمی‌کند و علت نامشخص. تصمیم: Rollback طبق Plan: بازگرداندن کابل/IP، تأیید Test Matrix روی OLD (۸ دقیقه). پس از آن RCA در Lab. درس: Rollback بر اساس زمان از پیش تعیین‌شده است نه عجله.

### ۷) پیاده‌سازی از مسیر CLI

``` text
diagnose sys session stat
get system session-ttl
```

### ۸) Verification (اثبات صحت)

- Test Matrix همه‌ی ردیف‌ها.
- Rollback آزمون شده.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| Session کمتر | Timeout | session-ttl |
| IPsec down | Proposal | تنظیم صریح |

### ۱۰) نکات امنیتی

- Backup رمزگذاری.

### ۱۱) جمع‌بندی مفهومی

- Baseline.
- Test Matrix.
- Rollback زمان‌دار.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) چرا Baseline؟ *(پاسخ: 30-4-ت1)*

**ت2.** (ساده) Rollback کی؟ *(پاسخ: 30-4-ت2)*

**ت3.** (متوسط) IPsec down پس از Cutover؛ علت؟ *(پاسخ: 30-4-ت3)*

**ت4.** (متوسط) Session کمتر؟ *(پاسخ: 30-4-ت4)*

**ت5.** (سخت) Rollback را آزمون کنید. *(پاسخ: 30-4-ت5)*

**ت6.** (سخت، طراحی) Plan T-7d تا T+1d. *(پاسخ: 30-4-ت6)*

**Q1.** Quick quiz (English): Why must the rollback plan be tested before cutover? *(پاسخ: 30-4-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| CHG | Change request | درخواست تغییر |

- *Test the rollback before the cutover.* ← Rollback را پیش از Cutover آزمون کنید.

### ۱۴) کارت Lab

**کارت Lab:** G11 (اجرا نشده). **Evidence:** `03-ops/g11-migration.md`.

### ۱۵) منابع

- Fortinet FortiOS 7.0 Administration Guide: Upgrade and migration

## پاسخ‌های فصل 30

> ابتدا بدون نگاه حل کنید. شناسه: درس-نوع+شماره (ت = تمرین، م = مرور).


### پاسخ‌های بازنویسی عمیق درس 30-1

**30-1-ت1** — تعداد دفعات Match یک Rule؛ برای شناسایی Ruleهای استفاده‌نشده.

**30-1-ت2** — تا قوانین مرده/پرریسک منتقل نشوند.

**30-1-ت3** — ASA بین سطوح امنیت پیش‌فرض اجازه می‌دهد؛ FortiGate Implicit deny.

**30-1-ت4** — IP داخلی (post-DNAT) چون DNAT قبل از Policy انجام می‌شود.

**30-1-ت5** — VIP/Policy NAT/IP Pool، Policy با آدرس درست، Test Matrix، بررسی Hairpin/ALG.

**30-1-ت6** — ستون‌ها: مبدأ، مقصد، Policy، NAT، Gap، Test؛ ۱۰ سطر.

**30-1-Q1** — Because the two platforms process traffic differently, so identical text can behave differently.


### پاسخ‌های بازنویسی عمیق درس 30-2

**30-2-ت1** — چک‌لیست تصمیم پیش از شروع؛ یک «No» ⇒ لغو.

**30-2-ت2** — شرط از پیش تعریف‌شده که بازگشت را الزامی می‌کند.

**30-2-ت3** — اگر مسیر اصلی قطع شود امکان بازگرداندن/مدیریت دستگاه باشد.

**30-2-ت4** — Test Matrix، Log/Session، Monitoring، آزمون مثبت/منفی.

**30-2-ت5** — اگر حیاتی: Rollback؛ وگرنه رفع محدود و ادامه؛ ثبت دلیل/زمان.

**30-2-ت6** — طبق قالب؛ با زمان‌بندی و مسئولان.

**30-2-Q1** — So the decision is made objectively before pressure and emotions affect judgment.


### پاسخ‌های بازنویسی عمیق درس 30-3


### پاسخ‌های بازنویسی عمیق درس 30-3

**30-3-ت1** — برای مقایسه.

**30-3-ت2** — حد قابل‌قبول Session.

**30-3-ت3** — Mapping اشتباه.

**30-3-ت4** — قابل‌قبول/بحرانی.

**30-3-ت5** — Rollback و RCA.

**30-3-ت6** — جدول.

**30-3-Q1** — To compare the state before and after the change with numbers.

### پاسخ‌های بازنویسی عمیق درس 30-4


### پاسخ‌های بازنویسی عمیق درس 30-4

**30-4-ت1** — برای مقایسه‌ی قبل/بعد.

**30-4-ت2** — طبق زمان و معیار از پیش تعیین‌شده.

**30-4-ت3** — Proposal پیش‌فرض متفاوت.

**30-4-ت4** — Timeout/Offload.

**30-4-ت5** — در Lab: بازگرداندن کابل/IP و Test Matrix.

**30-4-ت6** — طبق متن.

**30-4-Q1** — To be sure the old state can be restored within the change window.

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
