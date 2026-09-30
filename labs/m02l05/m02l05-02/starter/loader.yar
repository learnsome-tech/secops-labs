rule Loader_XorStub
{
    meta:
        author = "SOC detection team"
        description = "One-byte XOR decode loop plus loader strings"
        date = "2026-03-03"
    strings:
        $mutex = "Global\\Xq7-updater" ascii wide
        $gate  = "/gate.php" ascii
        $ps    = "powershell -nop -w hidden" ascii wide nocase
        $xor   = { 8A 04 ?? 34 ?? 88 04 ?? }
    condition:
        uint16(0) == 0x5A4D and filesize < 2MB and
        $xor and 2 of ($mutex, $gate, $ps)
}
