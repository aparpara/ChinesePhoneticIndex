# -*- coding: utf-8 -*-

import numpy as np
import os.path as op
import re
import pandas as pd
import unicodedata
from typing import Sequence


def entropy(x):
    x = np.asarray(x)
    x = x / x.sum()
    return np.where(x > 0, -x * np.log(x), 0).sum()


nan = float("nan")
PINYIN_ACCENTS = "\u0304\u0301\u030C\u0300"
GROUP_NAMES = ["uncommon", "rare", "minority", "majority"]


def put_accents(s):
    i = len(s)
    if not s.endswith("iu"):
        for c in "aoeêiuünm":
            i = s.find(c)
            if i >= 0:
                i += 1
                break
    yield s
    if i > 0:
        for a in PINYIN_ACCENTS:
            yield unicodedata.normalize("NFC", s[:i] + a + s[i:])


def strip_accents(s):
    s = "".join(c for c in unicodedata.normalize("NFD", s) if c not in PINYIN_ACCENTS)
    return unicodedata.normalize("NFC", s)


def get_tone(s):
    accent = [c for c in unicodedata.normalize("NFD", s) if c in PINYIN_ACCENTS]
    if len(accent) == 0:
        return 0
    assert len(accent) == 1
    res = PINYIN_ACCENTS.find(accent[0]) + 1
    assert res > 0
    return res


def pinyin_sort_key(x):
    return x.map(lambda s: (strip_accents(s), get_tone(s)))


def get_all_pinyin():
    table = {
        # fmt: off
        "a"   : ("", "y", "w", "b", "p", "m", "f", "d", "t", "n", "l", "g", "k", "h", "z", "c", "s", "zh", "ch", "sh"),
        "o"   : ("", "y", "w", "b", "p", "m", "f",                "l"),
        "e"   : ("", "y",                "m",      "d", "t", "n", "l", "g", "k", "h", "z", "c", "s", "zh", "ch", "sh", "r"),
        "ai"  : ("",      "w", "b", "p", "m",      "d", "t", "n", "l", "g", "k", "h", "z", "c", "s", "zh", "ch", "sh"),
        "ei"  : ("",      "w", "b", "p", "m", "f", "d", "t", "n", "l", "g", "k", "h", "z", "c",      "zh",       "sh"),
        "ao"  : ("", "y",      "b", "p", "m",      "d", "t", "n", "l", "g", "k", "h", "z", "c", "s", "zh", "ch", "sh", "r"),
        "ou"  : ("", "y",           "p", "m", "f", "d", "t", "n", "l", "g", "k", "h", "z", "c", "s", "zh", "ch", "sh", "r"),
        "an"  : ("", "y", "w", "b", "p", "m", "f", "d", "t", "n", "l", "g", "k", "h", "z", "c", "s", "zh", "ch", "sh", "r"),
        "en"  : ("",      "w", "b", "p", "m", "f", "d",      "n", "l", "g", "k", "h", "z", "c", "s", "zh", "ch", "sh", "r"),
        "ang" : ("", "y", "w", "b", "p", "m", "f", "d", "t", "n", "l", "g", "k", "h", "z", "c", "s", "zh", "ch", "sh", "r"),
        "eng" : ("",      "w", "b", "p", "m", "f", "d", "t", "n", "l", "g", "k", "h", "z", "c", "s", "zh", "ch", "sh", "r"),
        "ong" : (    "y", "w",                     "d", "t", "n", "l", "g", "k", "h", "z", "c", "s", "zh", "ch",       "r"),
        "i"   : (    "y",      "b", "p", "m",      "d", "t", "n", "l",                "z", "c", "s", "zh", "ch", "sh", "r", "j", "q", "x"),
        "ia"  : (                                  "d",      "n", "l",                                                      "j", "q", "x"),
        "iao" : (              "b", "p", "m", "f", "d", "t", "n", "l",                                                      "j", "q", "x"),
        "ie"  : (              "b", "p", "m",      "d", "t", "n", "l",                                                      "j", "q", "x"),
        "iu"  : (                        "m",      "d",      "n", "l",                                                      "j", "q", "x"),
        "ian" : (              "b", "p", "m",      "d", "t", "n", "l",                                                      "j", "q", "x"),
        "in"  : (    "y",      "b", "p", "m",      "d",      "n", "l",                                                      "j", "q", "x"),
        "iang": (              "b",                          "n", "l",                                                      "j", "q", "x"),
        "ing" : (    "y",      "b", "p", "m",      "d", "t", "n", "l",                                                      "j", "q", "x"),
        "iong": (                                                                                                           "j", "q", "x"),
        "u"   : (    "y", "w", "b", "p", "m", "f", "d", "t", "n", "l", "g", "k", "h", "z", "c", "s", "zh", "ch", "sh", "r", "j", "q", "x"),
        "ua"  : (                                                      "g", "k", "h",                "zh", "ch", "sh", "r"),
        "uo"  : (                                  "d", "t", "n", "l", "g", "k", "h", "z", "c", "s", "zh", "ch", "sh", "r"),
        "uai" : (                                                      "g", "k", "h",                "zh", "ch", "sh"),
        "ui"  : (                                  "d", "t",           "g", "k", "h", "z", "c", "s", "zh", "ch", "sh", "r"),
        "uan" : (    "y",                          "d", "t", "n", "l", "g", "k", "h", "z", "c", "s", "zh", "ch", "sh", "r", "j", "q", "x"),
        "un"  : (    "y",                          "d", "t", "n", "l", "g", "k", "h", "z", "c", "s", "zh", "ch", "sh", "r", "j", "q", "x"),
        "uang": (                                                      "g", "k", "h",                "zh", "ch", "sh"),
        "ue"  : (    "y",                                                                                                   "j", "q", "x"),
        "ü"   : (                                            "n", "l"),
        "üe"  : (                                            "n", "l"),
        "er"  : ("",),
        "n"   : ("",),
        "ng"  : ("", "h"),
        "m"   : ("", "h"),
        "ê"   : ("",),
        "r"   : ("",),
        # fmt: on
    }
    return {s for f, initials in table.items() for i in initials for s in put_accents(i + f)}


def read_unihan_table(filename, char_set=None, key_set=None):
    df = pd.read_csv(filename, sep="\t", header=0, comment="#", names=["char", "key", "val"])
    RE_UNICODE_CHAR = "U\+([0-9A-F]+)( [^U])?"

    def unicode_to_char(match):
        res = chr(int(match[1], base=16))
        if match[2] and match[2][1] != res:
            res += match[2]
        return res

    df["char"] = df.char.str.replace(RE_UNICODE_CHAR, unicode_to_char, regex=True)
    df["key"] = df.key.str[1:]
    df["val"] = df.val.str.replace(RE_UNICODE_CHAR, unicode_to_char, regex=True)

    if char_set is not None:
        df = df[df.char.isin(char_set)].reset_index(drop=True)
    if key_set is not None:
        df = df[df.key.isin(key_set)].reset_index(drop=True)

    return df


def read_unihan(root, char_set=None):
    dfv = read_unihan_table(op.join(root, "Unihan_Variants.txt"), char_set)
    dfv["val"] = dfv.val.str.replace("<[^ ]+", "", regex=True).str.replace(" ", "", regex=False)
    dfr = read_unihan_table(
        op.join(root, "Unihan_Readings.txt"),
        char_set,
        [
            "Definition",
            "HanyuPinlu",
            "HanyuPinyin",
            "Mandarin",
            "TGHZ2013",
            "XHC1983",
        ],
    )
    i = dfr.key.isin(["HanyuPinyin", "TGHZ2013", "XHC1983"])
    dfr.val[i] = (
        dfr.val[i]
        .str.replace("[0-9]+\.[0-9]+(,[0-9]+\.[0-9]+)*:", "", regex=True)
        .str.replace(",", " ", regex=False)
    )
    df = pd.concat([dfr, dfv]).pivot(index="char", columns="key", values="val")
    all_simpilfied = set("".join(df.SimplifiedVariant.dropna()))
    df["TraditionalOnly"] = ~(
        df.SimplifiedVariant.isna() | df.index.to_series(index=df.index).isin(all_simpilfied)
    )
    df.fillna("", inplace=True)
    re_freq = re.compile(r"\((\d+)\)")
    df["HanyuPinluFrequency"] = df.HanyuPinlu.apply(
        lambda s: sum(int(x) for x in re_freq.findall(s))
    )

    jd = pd.read_csv(
        op.join(root, "JunDaModern.txt"),
        sep="\t",
        comment="/",
        names=["no", "char", "freq", "cum_percent", "pinyin", "meaning"],
    )
    df["JunDaFrequency"] = 0
    df.loc[jd.char, "JunDaFrequency"] = jd.freq.to_numpy()
    df["JunDaReading"] = ""
    df.loc[jd.char, "JunDaReading"] = (
        jd.pinyin.fillna("").str.replace("/", " ", regex=False).to_list()
    )

    df["Frequency"] = df.HanyuPinluFrequency + df.JunDaFrequency
    return df


def get_statistics(df):
    return (
        len(df),
        df.replace("", nan).replace(0, nan).count(),
        df.filter(regex=".*Frequency").sum(),
    )


def merge_statistics(names, stats):
    def merge_one(vals):
        if all(isinstance(v, (pd.DataFrame, pd.Series)) for v in vals):
            return pd.concat(vals, axis=1, keys=names)
        return pd.DataFrame(
            {n: v if isinstance(v, Sequence) else (v,) for n, v in zip(names, vals)}
        )

    return tuple(merge_one(vals) for vals in tuple(zip(*stats)))


def n_readings(x):
    return x.str.count(" ") + (x.str.len() > 0)


def drop_extra_cols(df):
    empty = df.apply(lambda x: ~((x != "") & (x != 0)).any(), axis=0)
    return df.drop(
        columns=empty[empty].index.to_list() + ["SimplifiedVariant", "SpecializedSemanticVariant"]
    )


def markdown_with_col_name(df):
    indent = "\u2000" * max(len(df.index.name) - len(df.columns.name) // 2, 2)
    return df.rename_axis(index=f"\u200C{indent}{df.columns.name}<br>{df.index.name}").to_markdown()


def get_and_format_statistics(df):
    ds = df[~df.TraditionalOnly]
    dc = ds[ds.Frequency > 0]
    stats = merge_statistics(
        ("Total", "Simplified", "Counted"),
        (get_statistics(d) for d in (df, ds, dc)),
    )
    res = [
        ln
        for (header, fmtargs), stat in zip(
            (
                ("The total number of characters:", {"index": False}),
                (
                    "The number of non-empty and non-zero entries by column:",
                    {},
                ),
                ("The sum total frequency by column:", {"floatfmt": ",.0f"}),
            ),
            stats,
        )
        for ln in (header, stat.to_markdown(**fmtargs))
    ]
    df = df[~df.TraditionalOnly].drop(columns="TraditionalOnly")
    res.append("# In simplified characters")
    res.append(
        markdown_with_col_name(
            pd.crosstab(ds.HanyuPinluFrequency > 0, ds.JunDaFrequency > 0).rename_axis(
                index="In HanyuPinlu", columns="In JunDa"
            )
        )
    )
    x = ds.JunDaFrequency[ds.HanyuPinluFrequency == 0].sum() / ds.JunDaFrequency.sum() * 100
    res.append(f"By frequency, {x:.2f}% of JunDa characters are not in HanyuPinlu.")
    res.append("# In counted characters")
    res.append("In HanyuPinlu only:")
    res.append(
        drop_extra_cols(
            dc[dc.JunDaFrequency <= 0].sort_values("Frequency", ascending=False)
        ).to_markdown()
    )
    res.append("In JunDa only (top 100):")
    res.append(
        drop_extra_cols(
            dc[dc.HanyuPinluFrequency <= 0].sort_values("Frequency", ascending=False).iloc[:100]
        ).to_markdown()
    )
    res.append("With no pinyin:")
    res.append(
        drop_extra_cols(
            dc[dc.Mandarin == ""].sort_values("Frequency", ascending=False)
        ).to_markdown()
    )

    res.append("Number of readings according to different souces:")
    res.append(
        markdown_with_col_name(
            pd.crosstab(n_readings(dc.XHC1983), n_readings(dc.HanyuPinlu), margins="Both")
        )
    )
    res.append(
        markdown_with_col_name(
            pd.crosstab(n_readings(dc.TGHZ2013), n_readings(dc.HanyuPinlu), margins="Both")
        )
    )
    res.append(
        markdown_with_col_name(
            pd.crosstab(n_readings(dc.XHC1983), n_readings(dc.TGHZ2013), margins="Both")
        )
    )
    return res


def write_statistics(df, file_name="Statistics.md"):
    with open(file_name, "w", encoding="utf-8") as f:
        f.write("# Database Statistics\n\n")
        f.write("\n\n".join(get_and_format_statistics(df)))


def get_pinyin(s):
    if not s:
        return []
    return [x for x in s.replace(":", " ").split() if not x[0].isdecimal()]


def get_pinyin_pinlu(s):
    if not s:
        return []
    return [(r, int(f.rstrip(")"))) for rf in s.split() for r, f in (rf.split("(", 1),)]


def make_pinyin_database(df):
    def process_row(char, data):
        pinyin_data = [data.HanyuPinyin, data.TGHZ2013, data.XHC1983]
        if data.HanyuPinlu:
            res = {
                r: (
                    f + f * data.JunDaFrequency / data.HanyuPinluFrequency,
                    1 / i,
                )
                for i, (r, f) in enumerate(get_pinyin_pinlu(data.HanyuPinlu), 1)
            }
            pinyin_data.insert(0, data.Mandarin)
        else:
            res = {
                r: (data.JunDaFrequency, 1 / i) for i, r in enumerate(get_pinyin(data.Mandarin), 1)
            }
        for ds in pinyin_data:
            for i, r in enumerate(get_pinyin(ds), 1):
                f, k = res.get(r, (0, 0))
                res[r] = (f, k + 1 / i)
        return ({"char": char, "pinyin": r, "frequency": f, "rank": k} for r, (f, k) in res.items())

    return pd.DataFrame([item for row in df.iterrows() for item in process_row(*row)])


def make_pinyin_list(pdb):
    freq = pdb.frequency.sort_values(ascending=False)
    cum_freq = freq.cumsum()
    total_freq = cum_freq.iloc[-1]
    cum_freq /= total_freq
    thresholds = tuple(freq.iloc[(cum_freq <= t).sum()] for t in (0.95, 0.998)) + (0,)

    def process(df):
        df = df.sort_values(["frequency", "rank"], ascending=False)
        k = sum(df.frequency > t for t in thresholds)
        res = {
            gn: df.char[k == i].to_list() for i, gn in zip(range(len(thresholds) + 1), GROUP_NAMES)
        }
        res["frequency"] = df.frequency.sum() / total_freq
        res["entropy"] = entropy(df.frequency[df.frequency > 0])
        return pd.Series(res)

    res = pdb.groupby("pinyin").apply(process)
    res["bare_pinyin"] = [strip_accents(s) for s in res.index]
    for gn in GROUP_NAMES:
        res[f"n_{gn}"] = res[gn].str.len()
    return res


def make_pinyin_table(pl):
    pt = pl[["frequency", "entropy"]].copy().rename(columns={"frequency": "frequency, ‌‱"})
    pt["frequency, ‌‱"] *= 1000
    for gn in reversed(GROUP_NAMES):
        pt[gn] = pl.loc[pt.index, gn].apply(lambda x: "".join(x))
    return pt


def print_frequency_table(pl, stm):
    print("# Chinese Syllables Sorted by Frequency", file=stm)
    print(pl.sort_values("frequency, ‌‱", ascending=False).to_markdown(), file=stm)


def print_pinyin_table(pl, stm):
    print("# Chinese Syllables Sorted by Pinyin", file=stm)
    print(pl.sort_index(key=pinyin_sort_key).to_markdown(), file=stm)


def print_dictionary(pl, stm):
    print('#NAME\t"Chinese Phonetic Index"', file=stm)
    print('#INDEX_LANGUAGE\t"Chinese"', file=stm)
    print('#CONTENTS_LANGUAGE\t"Chinese"', file=stm)
    print('#ICON_FILE\t"ChPhoneticIndex.bmp"', file=stm)
    for bare_pinyin, df in pl.groupby("bare_pinyin"):
        print(bare_pinyin, file=stm)
        for pinyin, row in df.sort_index(key=pinyin_sort_key).iterrows():
            print("\t[m1]", pinyin, "[/m]", sep="", file=stm)
            for i, gn in enumerate(reversed(GROUP_NAMES), 1):
                chars = row[gn]
                if len(chars) > 0:
                    print(
                        f"\t[m2]{i}) [ref]",
                        "[/ref], [ref]".join(chars),
                        "[/ref][/m]",
                        sep="",
                        file=stm,
                    )


def generate_dictionary(df, out_dir="."):
    pl = make_pinyin_list(make_pinyin_database(df[~df.TraditionalOnly]))
    pt = make_pinyin_table(pl)
    with open(op.join(out_dir, "FrequencyTable.md"), "w", encoding="utf-8") as f:
        print_frequency_table(pt, f)
    with open(op.join(out_dir, "PinyinTable.md"), "w", encoding="utf-8") as f:
        print_pinyin_table(pt, f)
    with open(op.join(out_dir, "ChPhoneticIndex.dsl"), "w", encoding="utf-16") as f:
        print_dictionary(pl, f)


if __name__ == "__main__":
    from sys import argv

    input_dir = argv[1] if len(argv) > 1 else "."
    output_dir = argv[2] if len(argv) > 2 else "."

    df = read_unihan(input_dir)

    write_statistics(df, op.join(output_dir, "Statistics.md"))
    generate_dictionary(df, output_dir)
