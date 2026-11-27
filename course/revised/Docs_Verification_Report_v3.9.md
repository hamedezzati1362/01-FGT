# گزارش تطبیق دستورها با مستندات رسمی Fortinet (نسخه‌ی v3.9)

تاریخ: ۲۰۲۶-۱۱-۲۷ · روش: جست‌وجوی مستندات رسمی (docs.fortinet.com) و Fortinet Community · **هیچ دستگاهی اجرا نشد.**

> **معنی وضعیت «تأیید مستندی»:** دستور/پارامتر در مستندات رسمی (CLI Reference یا Administration Guide) وجود دارد. این **به معنی اجرا روی FortiOS 7.0.3 نیست**؛ فقط یعنی نام و ساختار دستور ساختگی نیست. اجرای واقعی همچنان فقط با Runbook Phase 0B ممکن است.

## ۱) دستورهای تأییدشده در مستندات

| دستور / پارامتر | وضعیت | نکته‌ی مهم | مرجع |
|---|---|---|---|
| `config firewall policy` → `tcp-mss-sender` / `tcp-mss-receiver` | تأیید مستندی | مقدار ۰ تا ۶۵۵۳۵، پیش‌فرض ۰؛ MSS = MTU − ۴۰ | [CLI Reference 7.0.3](https://docs.fortinet.com/document/fortigate/7.0.3/cli-reference/325620/config-firewall-policy) |
| `execute ha failover set / unset / status` | تأیید مستندی | فقط برای آزمون/نگهداری؛ Flag تا `unset` می‌ماند؛ ID خوشه اختیاری | [execute ha](https://docs.fortinet.com/document/fortigate/7.2.13/cli-reference/105234857/execute-ha) |
| `config system vdom-link` (`edit`، `set type ppp\|ethernet\|npupair`) | تأیید مستندی | نام حداکثر ۱۱ نویسه؛ پیش‌فرض ppp؛ Interface با `type vdom-link` ساخته می‌شود | [vdom-link 7.0.11](https://docs.fortinet.com/document/fortigate/7.0.11/cli-reference/5620/config-system-vdom-link) |
| `config log setting` → `fwpolicy-implicit-log` | تأیید مستندی | پیش‌فرض disable؛ جایگزین: Deny صریح با Log | [log setting](https://docs.fortinet.com/document/fortigate/7.2.12/cli-reference/196223761/config-log-setting) |
| `diagnose test authserver ldap <server> <user> <pass>` | تأیید مستندی | نام Object LDAP نه نام میزبان؛ برای جزئیات `diagnose debug application fnbamd 255` | [diagnose test authserver](https://docs.fortinet.com/document/fortigate/7.6.4/cli-reference/283783396/diagnose-test-authserver) |
| SD-WAN: `failtime` / `recoverytime` | تأیید مستندی | محدوده ۱ تا ۳۶۰۰؛ پیش‌فرض ۵؛ حداقل توصیه‌ی failtime=۲ | [sdwan 7.0.7](https://docs.fortinet.com/document/fortigate/7.0.7/cli-reference/92620/config-system-sdwan) |
| SD-WAN: `config service` / `mode` | تأیید مستندی با تفاوت نسخه | ۷.۰.۰: `mode priority`؛ ۷.۰.۷ تا ۷.۰.۱۲: auto/manual/priority/sla/load-balance | [sdwan 7.0.12](https://docs.fortinet.com/document/fortigate/7.0.12/cli-reference/74620) |
| `config system global` → `admin-lockout-threshold` / `admin-lockout-duration` | تأیید مستندی | threshold ۱–۱۰ (پیش‌فرض ۳)؛ duration پیش‌فرض ۶۰ ثانیه | [system global 7.0.11](https://docs.fortinet.com/document/fortigate/7.0.11/cli-reference/1620/config-system-global) |
| `cfg-save revert` و `cfg-revert-timeout` | تأیید مستندی | پیش‌فرض timeout ۶۰۰ ثانیه؛ ذخیره‌ی دستی و بازگشت خودکار | [system global](https://docs.fortinet.com/document/fortigate/7.2.3/cli-reference/1620/config-system-global) |
| `diagnose sys ha history read`، `ha checksum cluster`، `get system ha status` | تأیید مستندی | مجموعه‌ی استاندارد عیب‌یابی HA | [diagnose sys](https://docs.fortinet.com/document/fortigate/7.6.2/cli-reference/235530229/diagnose-sys) |
| `config system link-monitor` (`srcintf`، `server`، `gateway-ip`، `failtime`، `recoverytime`، `update-static-route`) | تأیید مستندی | failtime/recoverytime پیش‌فرض ۵؛ update-static-route پیش‌فرض enable | [link-monitor 7.0.10](https://docs.fortinet.com/document/fortigate/7.0.10/cli-reference/120620/config-system-link-monitor) |
| `diagnose vpn ike gateway list`، `diagnose vpn tunnel list`، `diagnose debug application ike -1` | تأیید مستندی | `log-filter` با خط‌تیره تا قبل 7.4.1؛ از 7.4.1 `log filter` با فاصله | [IPsec diagnose](https://docs.fortinet.com/document/fortigate/7.4.9/administration-guide/044240/ipsec-related-diagnose-commands) |
| `diagnose debug flow ...` و Offload | تأیید مستندی | ترافیک Offload‌شده به NP6/NP7 دیده نمی‌شود؛ غیرفعال‌سازی Offload یا آزمون با ICMP | [Debugging the packet flow](https://docs.fortinet.com/document/fortigate/7.6.4/administration-guide/54688/debugging-the-packet-flow) |
| `config vpn ssl settings` (`tunnel-ip-pools`، `source-interface`، `default-portal`) | تأیید مستندی | نام گزینه‌ها بین پچ‌های ۷.۰ کمی فرق می‌کند | [vpn ssl settings 7.0.3](https://docs.fortinet.com/document/fortigate/7.0.3/cli-reference/363620/config-vpn-ssl-settings) |

## ۲) اصلاحات لازم پس از تطبیق

1. **`diagnose vpn ike log-filter`:** در 7.0.3 با خط‌تیره درست است؛ از 7.4.1 به `log filter` (با فاصله) تغییر کرده. نام فیلتر مبدأ در مستندات جدید `rem-addr4` است (در درس‌ها `dst-addr4` آمده؛ هر دو را با CLI help همان نسخه بررسی کنید).
2. **سطح Debug برای fnbamd:** مستندات 255 را می‌گویند؛ در درس‌ها -1 هم آمده. هر دو رایج‌اند؛ 255 را ترجیح دهید.
3. **`auto-asic-offload` روی Policy:** در جست‌وجو نحو دقیق پیدا نشد؛ با CLI Reference همان نسخه تأیید شود. راه مستند: غیرفعال‌سازی Offload NP یا آزمون با ICMP.
4. **`execute ha failover set`:** فقط برای آزمون است و Flag تا `unset` باقی می‌ماند؛ در Production از `diagnose sys ha reset-uptime` یا روش مستند استفاده شود.
5. **SD-WAN `mode`:** در 7.0.0 نمونه‌ی مستند `mode priority` دارد؛ در پچ‌های بعدی `sla` هم هست. نسخه‌ی دقیق Image را بسنجید.

## ۳) هنوز تأیید نشده (نیازمند جست‌وجوی بعدی یا اجرا)

- `session-pickup-connectionless` / `session-pickup-nat` (درس ۲۲-۳).
- `execute ha synchronize start` (درس ۲۲-۲).
- `diagnose firewall iprope lookup` (در این دور جست‌وجو نشد).
- `diagnose test application dnsproxy 3`.
- نام دقیق پارامترهای SNMPv3 (`auth-proto`، `priv-proto`) در 7.0.3.
- Config IKEv2 سمت Cisco IOS-XE 17.03 (جدا از Fortinet).

## ۴) نتیجه

بیشتر دستورهای پرکاربرد وجود دارند و نام/ساختارشان درست است. تفاوت‌های مهم نسخه (7.4.1 برای IKE log filter و Failtime/Recoverytime SD-WAN، 7.6.3 برای SSL-VPN) در متن درس‌ها آمده است. **هیچ دستور هنوز «اجراشده با شاهد» نیست.**
