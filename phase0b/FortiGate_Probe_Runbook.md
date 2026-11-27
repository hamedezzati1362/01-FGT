# Runbook راستی‌آزمایی دستورهای FortiGate (Phase 0B — اجرا توسط کاربر)

> **قاعده‌ها:** (۱) فقط روی FortiGate VM داخل Lab ایزوله (`vSwitch-FGT` بدون Uplink) اجرا شود. (۲) پیش از شروع Snapshot و `execute backup config` بگیرید. (۳) هیچ رمزی در خروجی‌ها/ریپو ذخیره نشود. (۴) Claude هیچ فرمانی را اجرا نمی‌کند؛ شما اجرا می‌کنید و خروجی را در فایل Evidence می‌گذارید. (۵) هر ردیف یکی از وضعیت‌های **Tested-OK** (خروجی مطابق انتظار)، **CLI-Accepted** (پذیرفته شد ولی رفتار آزمایش نشد)، **Fail** (خطا) یا **Untested (لایسنس/ابزار لازم)** می‌گیرد.

## ۱) پیش‌آزمون (اجباری)

``` text
get system status
get system performance status
diagnose hardware deviceinfo nic port1
show system interface
```

ثبت: Version/Build (باید 7.0.3 یا نسخه‌ی واقعی Image)، Serial، License Status، Operation Mode، Virtual domain.

اگر نسخه 7.0.3 نبود، همه‌ی ردیف‌های زیر نسبت به **نسخه‌ی واقعی** ثبت شود و در درس‌ها «اختلاف نسخه» نوشته شود.

## ۲) جدول Probe (مرتب بر اساس درس)

| # | درس | دستور (روی FortiGate) | انتظار | وضعیت | یادداشت |
|---|---|---|---|---|---|
| 1 | 12-1 | `get system status` | Version/Serial/License | | |
| 2 | 12-1 | `diagnose sys ntp status` | sync یا unsynced | | |
| 3 | 12-2 | `config system interface` / `set allowaccess ping` / `end` | پذیرفته | | |
| 4 | 12-2 | `get system interface physical` | لینک‌ها | | |
| 5 | 12-4 | `get router info routing-table all` | جدول مسیر | | |
| 6 | 12-4 | `config system link-monitor` (ساخت و حذف) | پذیرفته | | |
| 7 | 12-5 | `config system global` / `set admin-lockout-threshold 3` | پذیرفته | | |
| 8 | 12-6 | `execute backup config tftp <file> <server>` | فایل ساخته | | |
| 9 | 13-1 | `diagnose firewall iprope lookup <src> <sport> <dst> <dport> tcp <intf>` | Policy ID | | |
| 10 | 13-2 | `config firewall ippool` (type overload) | پذیرفته | | |
| 11 | 13-3 | `config firewall vip` (portforward) | پذیرفته | | |
| 12 | 13-4 | `diagnose sys session filter ...` / `session list` | Session | | |
| 13 | 13-4 | `get system session-ttl` | مقادیر | | |
| 14 | 14-2 | `diagnose sniffer packet any 'icmp' 4 5 l` | بسته‌ها | | |
| 15 | 14-3 | `diagnose debug flow ...` (فقط ۵ بسته) و `disable` | خط Allowed/Denied | | |
| 16 | 14-4 | `diagnose firewall proute list` | فهرست | | |
| 17 | 14-5 | `execute ping-options df-bit yes` + `data-size` | پذیرفته | | |
| 18 | 11-5 | `set tcp-mss-sender 1360` روی Policy | پذیرفته؟ | | |
| 19 | 16 | `diagnose autoupdate versions` | وضعیت FortiGuard | | |
| 20 | 17-7 | `diagnose test authserver ldap <srv> <user> <pw>` | نتیجه | | |
| 21 | 18 | `diagnose vpn ike gateway list` | وضعیت | | |
| 22 | 18 | `diagnose vpn tunnel list` | وضعیت | | |
| 23 | 18 | `diagnose debug application ike -1` + `disable` | Debug | | |
| 24 | 20 | `get vpn ssl monitor` | فهرست | | |
| 25 | 21 | `diagnose sys sdwan health-check` | وضعیت | | |
| 26 | 21 | `diagnose sys sdwan member` / `service` | وضعیت | | |
| 27 | 22 | `get system ha status` | Standalone یا Cluster | | |
| 28 | 22 | `diagnose sys ha checksum cluster` | (Needs HA) | | |
| 29 | 24 | `config system vdom-link` | (Needs VDOM) | | |
| 30 | 27 | `config log syslogd setting` | پذیرفته | | |
| 31 | 27 | `config system snmp user` (auth-priv) | پذیرفته | | |
| 32 | 12-5 | `config system accprofile` | پذیرفته | | |
| 33 | 15 | `config firewall policy` (نمونه‌ی Policy 62) | پذیرفته | | |
| 34 | 13-5 | `config firewall schedule recurring` | پذیرفته | | |
| 35 | 12-3 | `config system zone` و `config firewall address` | پذیرفته | | |

> ردیف‌های Needs-License (HA، VDOM، FMG/FAZ، FortiGuard) اگر در Eval فعال نیستند **Untested** ثبت شوند؛ نه Fail.

## ۳) نحوه‌ی ثبت Evidence

برای هر ردیف: خروجی (بدون رمز) در `phase0b/evidence/NN_<name>.txt` + زمان + وضعیت. سپس خلاصه‌ی وضعیت‌ها در `phase0b/probe_results.md` (قالب بالا).

## ۴) بعد از Probe (کار Claude)

۱. تغییر برچسب `Unverified` فقط برای ردیف‌های **Tested-OK** به «اجراشده با شاهد» با ارجاع به Evidence. ۲. ردیف‌های Fail/اختلاف نسخه در درس‌ها اصلاح و در DECISIONS_LOG ثبت. ۳. نسخه‌ی v4.0 با گزارش «قبل/بعد راستی‌آزمایی».

## ۵) ایمنی

- پیش از هر `config ... delete/unset` Snapshot.
- `diagnose debug` فقط با `trace start 5` و پس از آن `diagnose debug disable` + `diagnose debug reset`.
- ترافیک واقعی به اینترنت/شبکه‌ی کاری نفرستید (Uplink ندارد).
