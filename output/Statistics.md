# Database Statistics

The total number of characters:

|   Total |   Simplified |   Counted |
|--------:|-------------:|----------:|
|   46150 |        39840 |      8360 |

The number of non-empty and non-zero entries by column:

| key                        |   Total |   Simplified |   Counted |
|:---------------------------|--------:|-------------:|----------:|
| Definition                 |   23259 |        19086 |      7626 |
| HanyuPinlu                 |    3799 |         2843 |      2843 |
| HanyuPinyin                |   34130 |        28788 |      5734 |
| Mandarin                   |   41419 |        35633 |      8358 |
| SemanticVariant            |    3417 |         2504 |      1317 |
| SimplifiedVariant          |    6742 |          432 |       423 |
| SpecializedSemanticVariant |     523 |          389 |       264 |
| SpoofingVariant            |     295 |          255 |        56 |
| TGHZ2013                   |    8105 |         8094 |      6969 |
| TraditionalVariant         |    6289 |         6289 |      2517 |
| XHC1983                    |   11072 |         9384 |      7276 |
| ZVariant                   |     139 |          100 |        33 |
| TraditionalOnly            |   46150 |        39840 |      8360 |
| HanyuPinluFrequency        |    3799 |         2843 |      2843 |
| JunDaFrequency             |    9933 |         8352 |      8352 |
| JunDaReading               |    9901 |         8324 |      8324 |
| Frequency                  |   10416 |         8360 |      8360 |
| Rank                       |    8360 |         8360 |      8360 |

The sum total frequency by column:

| key                 |       Total |   Simplified |     Counted |
|:--------------------|------------:|-------------:|------------:|
| HanyuPinluFrequency |   2,191,752 |    1,713,523 |   1,713,523 |
| JunDaFrequency      | 193,504,018 |  193,460,816 | 193,460,816 |
| Frequency           | 195,695,770 |  195,174,339 | 195,174,339 |

# In simplified characters

| ‌         In JunDa<br>In HanyuPinlu   |   False |   True |
|:-------------------------------------|--------:|-------:|
| False                                |   31480 |   5517 |
| True                                 |       8 |   2835 |

By frequency, 2.27% of JunDa characters are not in HanyuPinlu.

# In counted characters

In HanyuPinlu only:

| char   | Definition                        | HanyuPinlu   | HanyuPinyin   | Mandarin   | SemanticVariant   | TGHZ2013   | XHC1983   |   HanyuPinluFrequency |   Frequency |   Rank |
|:-------|:----------------------------------|:-------------|:--------------|:-----------|:------------------|:-----------|:----------|----------------------:|------------:|-------:|
| 朮     | skill, art; method; trick, device | shù(1056)    | zhú           | shù        |                   |            |           |                  1056 |        1056 |   3485 |
| 淨     | pure, clean, unspoiled            | jìng(152)    | chéng jìng    | jìng       | 凈                |            | jìng      |                   152 |         152 |   5163 |
| 僱     | employ, hire                      | gù(25)       |               | gù         | 雇                |            | gù        |                    25 |          25 |   6376 |
| 羨     | envy, admire; praise; covet       | xiàn(24)     |               | xiàn       | 羡                |            | xiàn      |                    24 |          24 |   6397 |
| 淒     | bitter cold, miserable, dreary    | qī(16)       | qī qiàn       | qī         | 凄                |            | qī        |                    16 |          16 |   6558 |
| 嗐     | alas!                             | hài(14)      | hài           | hài        |                   | hài        | hài       |                    14 |          14 |   6604 |
| 犛     | a black ox, a yak                 | máo(11)      | máo lí        | máo        |                   |            | lí        |                    11 |          11 |   6692 |
| 痺     | paralysis, numbness               | bì(10)       |               | bì         | 痹                |            | bì        |                    10 |          10 |   6732 |

In JunDa only (top 100):

| char   | Definition                                                               | HanyuPinyin                                | Mandarin   | SemanticVariant   | TGHZ2013   | TraditionalVariant   | XHC1983   | ZVariant   |   JunDaFrequency | JunDaReading   |   Frequency |   Rank |
|:-------|:-------------------------------------------------------------------------|:-------------------------------------------|:-----------|:------------------|:-----------|:---------------------|:----------|:-----------|-----------------:|:---------------|------------:|-------:|
| 罗     | net for catching birds; gauze                                            |                                            | luō        | 羅                | luó        | 罗羅                 | luō luó   |            |           108376 | luo1           |      108376 |    395 |
| 京     | capital city                                                             | jīng                                       | jīng       |                   | jīng       |                      | jīng      |            |            71245 | jing1          |       71245 |    569 |
| 兰     | orchid; elegant, graceful                                                |                                            | lán        |                   | lán        | 蘭                   | lán       |            |            61951 | lan2           |       61951 |    648 |
| 尼     | Buddhist nun; transliteration                                            | ní nǐ                                      | ní         |                   | ní         |                      | ní        |            |            60474 | ni2            |       60474 |    657 |
| 刘     | surname; kill, destroy                                                   |                                            | liú        | 劉                | liú        | 刘劉                 | liú       |            |            48600 | liu2           |       48600 |    755 |
| 恩     | kindness, mercy, charity                                                 | ēn                                         | ēn         | 摁                | ēn         |                      | ēn        |            |            37898 | en1            |       37898 |    892 |
| 鲁     | foolish, stupid, rash; vulgar                                            |                                            | lǔ         |                   | lǔ         | 魯                   | lǔ        |            |            37474 | lu3            |       37474 |    899 |
| 泽     | marsh, swamp; grace, brilliance                                          |                                            | zé         |                   | zé         | 澤                   | zé        |            |            34311 | ze2            |       34311 |    955 |
| 诺     | promise; assent, approve                                                 |                                            | nuò        |                   | nuò        | 諾                   | nuò       |            |            32991 | nuo4           |       32991 |    971 |
| 伦     | normal human relationships                                               |                                            | lún        |                   | lún        | 倫                   | lún       |            |            32822 | lun2           |       32822 |    972 |
| 奥     | mysterious, obscure, profound                                            | ào yù yōu                                  | ào         |                   | ào         | 奧                   | ào        |            |            32761 | ao4            |       32761 |    973 |
| 唐     | Tang dynasty; Chinese                                                    | táng                                       | táng       |                   | táng       |                      | táng      |            |            32757 | tang2          |       32757 |    974 |
| 洛     | river in Shanxi province; city                                           | luò                                        | luò        |                   | luò        |                      | luò       |            |            32431 | luo4           |       32431 |    982 |
| 宋     | Song dynasty; surname                                                    | sòng                                       | sòng       |                   | sòng       |                      | sòng      |            |            31748 | song4          |       31748 |    997 |
| 川     | stream, river; flow; boil                                                | chuān                                      | chuān      | 巛                | chuān      |                      | chuān     |            |            25575 | chuan1         |       25575 |   1113 |
| 朱     | cinnabar, vermilion; surname                                             | zhū shū                                    | zhū        |                   | zhū        | 朱硃                 | zhū       |            |            25195 | zhu1           |       25195 |   1123 |
| 吴     | name of warring state; surname                                           | wú tūn                                     | wú         |                   | wú         | 吳吴                 | wú        | 吳呉       |            24632 | wu2            |       24632 |   1139 |
| 雅     | elegant, graceful, refined                                               | yā yǎ yá                                   | yǎ         |                   | yǎ         |                      | yā yǎ     |            |            24527 | ya3            |       24527 |   1144 |
| 赵     | surname; ancient state                                                   |                                            | zhào       |                   | zhào       | 趙                   | zhào      |            |            23428 | zhao4          |       23428 |   1170 |
| 蒋     | surname; Hydropyrum latifolium                                           |                                            | jiǎng      |                   | jiǎng      | 蔣                   | jiǎng     |            |            23237 | jiang3         |       23237 |   1176 |
| 耶     | used in transliteration                                                  | yé xié yē                                  | yé         |                   | yē yé      |                      | yē yé     |            |            23175 | ye1            |       23175 |   1178 |
| 莱     | goosefoot, weed; fallow field                                            |                                            | lái        |                   | lái        | 萊                   | lái       |            |            22187 | lai2           |       22187 |   1201 |
| 侠     | chivalrous person; knight-errant                                         |                                            | xiá        |                   | xiá        | 侠俠                 | xiá       |            |            20999 | xia2           |       20999 |   1222 |
| 韩     | fence; surname; Korea                                                    |                                            | hán        |                   | hán        | 韓                   | hán       |            |            20947 | han2           |       20947 |   1225 |
| 曼     | long, extended, vast; beautiful                                          | màn                                        | màn        | 㬅                | màn        |                      | màn       |            |            20897 | man4           |       20897 |   1229 |
| 玛     | agate; cornelian                                                         |                                            | mǎ         |                   | mǎ         | 瑪                   | mǎ        |            |            20207 | ma3            |       20207 |   1254 |
| 弗     | not, negative                                                            | fú                                         | fú         |                   | fú         |                      | fú        |            |            19905 | fu2            |       19905 |   1262 |
| 艾     | artemisia, mugwort                                                       | ài yì                                      | ài         |                   | ài yì      |                      | ài yì     |            |            18825 | ai4            |       18825 |   1297 |
| 泰     | great, exalted, superior; big; hexagram ䷊                                | tài                                        | tài        |                   | tài        |                      | tài       |            |            18069 | tai4           |       18069 |   1323 |
| 瑞     | felicitous omen; auspicious                                              | ruì                                        | ruì        |                   | ruì        |                      | ruì       |            |            17869 | rui4           |       17869 |   1341 |
| 赫     | bright, radiant, glowing                                                 | hè shì                                     | hè         |                   | hè         |                      | hè        |            |            17613 | he4            |       17613 |   1350 |
| 仁     | humaneness, benevolence, kindness                                        | rén                                        | rén        |                   | rén        |                      | rén       |            |            17263 | ren2           |       17263 |   1363 |
| 秦     | feudal state of Qin; the Qin dynasty (from which the name 'China' comes) | qín                                        | qín        |                   | qín        |                      | qín       |            |            16088 | qin2           |       16088 |   1399 |
| 菲     | fragrant, luxuriant; the Philippines                                     | fěi fèi fēi                                | fēi        |                   | fēi fěi    |                      | fēi fěi   |            |            15365 | fei1           |       15365 |   1423 |
| 蒂     | peduncle or stem of plants                                               | dì                                         | dì         |                   | dì         |                      | dì        |            |            15183 | di4            |       15183 |   1442 |
| 迪     | enlighten, advance; progress                                             | dí                                         | dí         | 廸                | dí         |                      | dí        |            |            15073 | di2            |       15073 |   1447 |
| 霍     | quickly, suddenly; surname                                               | huò hè suǒ                                 | huò        |                   | huò        |                      | huò       |            |            15034 | huo4           |       15034 |   1450 |
| 凯     | triumphant; triumph, victory                                             |                                            | kǎi        |                   | kǎi        | 凱                   | kǎi       |            |            14990 | kai3           |       14990 |   1455 |
| 郎     | gentleman, young man; husband                                            | láng                                       | láng       |                   | láng làng  |                      | láng làng | 郞         |            14845 | lang2          |       14845 |   1462 |
| 券     | certificate, ticket; title deeds                                         | quàn xuàn                                  | quàn       |                   | quàn xuàn  |                      | quàn xuàn |            |            14293 | quan4          |       14293 |   1483 |
| 乔     | tall, lofty; proud, stately                                              |                                            | qiáo       | 喬                | qiáo       | 乔喬                 | qiáo      |            |            14107 | qiao2          |       14107 |   1492 |
| 腊     | year-end sacrifice; dried meat                                           | xī là                                      | là         | 臈臘              | là         | 腊臘                 | là xī     |            |            13892 | la4            |       13892 |   1503 |
| 彭     | name of ancient country; surname                                         | péng páng bāng pēng                        | péng       |                   | péng       |                      | péng      |            |            13866 | peng2          |       13866 |   1505 |
| 媒     | go-between, matchmaker; medium                                           | méi mèi                                    | méi        |                   | méi        |                      | méi       |            |            13802 | mei2           |       13802 |   1510 |
| 惠     | favor, benefit, confer kindness                                          | huì                                        | huì        |                   | huì        |                      | huì       |            |            13492 | hui4           |       13492 |   1524 |
| 邪     | wrong, evil, depraved, vicious, perverse, heterodox                      | yá xié yé xú shé                           | xié        |                   | xié        |                      | xié yé    |            |            12952 | xie2           |       12952 |   1544 |
| 曹     | ministry officials; surname                                              | cáo                                        | cáo        |                   | cáo        |                      | cáo       |            |            12443 | cao2           |       12443 |   1575 |
| 孟     | first in series; great, eminent                                          | mèng                                       | mèng       |                   | mèng       |                      | mèng      |            |            12274 | meng4          |       12274 |   1581 |
| 娜     | elegant, graceful, delicate                                              | nuó nà                                     | nà         |                   | nà nuó     |                      | nà nuó    |            |            12060 | nuo2           |       12060 |   1588 |
| 芳     | fragrant; virtuous; beautiful                                            | fāng                                       | fāng       |                   | fāng       |                      | fāng      |            |            12015 | fang1          |       12015 |   1593 |
| 贷     | lend; borrow; pardon                                                     |                                            | dài        |                   | dài        | 貸                   | dài       |            |            11793 | dai4           |       11793 |   1612 |
| 昌     | light of sun; good, proper                                               | chāng chàng                                | chāng      |                   | chāng      |                      | chāng     |            |            11787 | chang1         |       11787 |   1613 |
| 邓     | surname                                                                  | shān dèng                                  | dèng       |                   | dèng       | 鄧                   | dèng      |            |            11651 | deng4          |       11651 |   1621 |
| 廷     | court                                                                    | tíng                                       | tíng       |                   | tíng       |                      | tíng      |            |            11499 | ting2          |       11499 |   1629 |
| 澳     | inlet, bay; dock, bank                                                   | yù ào                                      | ào         | 襖𥜌              | ào         |                      | ào        |            |            11475 | ao4            |       11475 |   1630 |
| 董     | direct, supervise; surname                                               | dǒng zhǒng                                 | dǒng       |                   | dǒng       |                      | dǒng      |            |            11450 | dong3          |       11450 |   1634 |
| 幽     | quiet, secluded, tranquil; dark                                          | yōu                                        | yōu        |                   | yōu        |                      | yōu       |            |            11319 | you1           |       11319 |   1643 |
| 辖     | linchpin of wheel; control                                               |                                            | xiá        |                   | xiá        | 轄                   | xiá       |            |            11213 | xia2           |       11213 |   1651 |
| 晋     | advance, increase; promote                                               |                                            | jìn        | 晉                | jìn        | 晉晋                 | jìn       |            |            11192 | jin4           |       11192 |   1653 |
| 魏     | kingdom of Wei; surname                                                  | wèi wéi wēi                                | wèi        | 巍                | wèi        |                      | wèi       |            |            11161 | wei4           |       11161 |   1655 |
| 吾     | i, my, our; resist, impede                                               | wú yú yá                                   | wú         |                   | wú         |                      | wú        |            |            11154 | wu2            |       11154 |   1656 |
| 韦     | tanned leather; surname; simplified form of Kangxi radical 178           |                                            | wéi        |                   | wéi        | 韋                   | wéi       |            |            10882 | wei2           |       10882 |   1670 |
| 筹     | chip, tally, token; raise money                                          |                                            | chóu       |                   | chóu       | 籌                   | chóu      |            |            10671 | chou2          |       10671 |   1681 |
| 沈     | sink, submerge; addicted to; surname                                     | chén shěn tán                              | shěn chén  | 沉                | shěn       | 沈瀋                 | chén shěn |            |            10628 | chen2          |       10628 |   1685 |
| 阁     | chamber, pavilion; cabinet                                               |                                            | gé         |                   | gé         | 閣                   | gé        |            |            10595 | ge2            |       10595 |   1688 |
| 旨     | purpose, aim; excellent                                                  | zhǐ                                        | zhǐ        |                   | zhǐ        |                      | zhǐ       |            |            10590 | zhi3           |       10590 |   1689 |
| 瑟     | large stringed musical instrument; dignified, massive; sound of wind     | sè                                         | sè         |                   | sè         |                      | sè        |            |            10473 | se4            |       10473 |   1699 |
| 戈     | halberd, spear, lance; rad. 62                                           | gē                                         | gē         |                   | gē         |                      | gē        |            |            10456 | ge1            |       10456 |   1700 |
| 仲     | middle brother; go between, mediator; surname                            | zhòng                                      | zhòng      |                   | zhòng      |                      | zhòng     |            |            10316 | zhong4         |       10316 |   1711 |
| 卢     | cottage, hut; surname; black                                             |                                            | lú         |                   | lú         | 盧                   | lú        |            |            10266 | lu2            |       10266 |   1714 |
| 冠     | cap, crown, headgear                                                     | guān guàn                                  | guān       |                   | guān guàn  |                      | guān guàn |            |            10217 | guan1          |       10217 |   1716 |
| 吕     | surname; a musical note                                                  | lǚ                                         | lǚ         |                   | lǚ         | 呂                   | lǚ        |            |            10156 | lu:3           |       10156 |   1719 |
| 玄     | deep, profound, abstruse; Kangxi radical 95                              | xuán xuàn                                  | xuán       | 伭                | xuán       |                      | xuán      |            |            10151 | xuan2          |       10151 |   1720 |
| 冯     | surname; gallop; by dint of                                              |                                            | féng       |                   | féng       | 馮                   | féng píng |            |            10128 | feng2          |       10128 |   1724 |
| 敦     | esteem; honest, candid, sincere                                          | dūn duī tuán diāo dùn dào zhǔn tūn duì tún | dūn        | 惇                | dūn        |                      | duì dūn   |            |            10084 | dun1           |       10084 |   1733 |
| 凌     | pure; virtuous; insult; maltreat                                         | lìng líng                                  | líng       |                   | líng       |                      | líng      |            |             9999 | ling2          |        9999 |   1735 |
| 恭     | respectful, polite, reverent                                             | gōng                                       | gōng       |                   | gōng       |                      | gōng      |            |             9787 | gong1          |        9787 |   1748 |
| 赋     | tax; give; endow; army; diffuse                                          |                                            | fù         |                   | fù         | 賦                   | fù        |            |             9723 | fu4            |        9723 |   1756 |
| 袁     | robe; surname                                                            | yuán                                       | yuán       |                   | yuán       |                      | yuán      |            |             9609 | yuan2          |        9609 |   1763 |
| 侯     | marquis, lord; target in archery                                         | hóu hòu                                    | hóu        |                   | hóu hòu    |                      | hóu hòu   |            |             9585 | hou2           |        9585 |   1765 |
| 兹     | now, here; this; time, year                                              |                                            | zī         | 玆茲              | cí zī      | 茲                   | cí zī     |            |             9319 | zi1            |        9319 |   1785 |
| 祭     | sacrifice to, worship                                                    | jì zhài                                    | jì         |                   | jì zhài    |                      | jì zhài   |            |             9316 | ji4            |        9316 |   1786 |
| 履     | footwear, shoes; walk on, tread; hexagram ䷉                              | lǚ                                         | lǚ         |                   | lǚ         |                      | lǚ        |            |             9091 | lu:3           |        9091 |   1806 |
| 坛     | altar; arena, examination hall                                           |                                            | tán        | 壇                | tán        | 坛壇罈罎             | tán       |            |             9049 | tan2           |        9049 |   1811 |
| 仆     | fall forward; lie prostrate, prone; servant                              | pū pú                                      | pū         |                   | pū pú      | 仆僕                 | pū pú     |            |             8976 | pu1            |        8976 |   1815 |
| 郭     | outer part (of a city); surname                                          | guō guó                                    | guō        |                   | guō        |                      | guō       |            |             8931 | guo1           |        8931 |   1817 |
| 契     | deed, contract, bond; engrave                                            | qì xiè qiè jié                             | qì         |                   | qì         |                      | qì xiè    |            |             8845 | qi4            |        8845 |   1825 |
| 劫     | take by force, coerce; disaster                                          | jié                                        | jié        | 刦刧刼            | jié        |                      | jié       |            |             8752 | jie2           |        8752 |   1831 |
| 赢     | win; surplus, gain, profit                                               |                                            | yíng       |                   | yíng       | 贏                   | yíng      |            |             8657 | ying2          |        8657 |   1843 |
| 莲     | lotus, water lily; paradise                                              |                                            | lián       |                   | lián       | 蓮                   | lián      |            |             8650 | lian2          |        8650 |   1845 |
| 岳     | mountain peak; surname                                                   | yuè                                        | yuè        |                   | yuè        |                      | yuè       |            |             8577 | yue4           |        8577 |   1852 |
| 嘉     | excellent; joyful; auspicious                                            | jiā                                        | jiā        |                   | jiā        |                      | jiā       |            |             8576 | jia1           |        8576 |   1853 |
| 俊     | talented, capable; handsome                                              | jùn shùn dūn                               | jùn        |                   | jùn        |                      | jùn       |            |             8543 | jun4           |        8543 |   1857 |
| 妖     | strange, weird, supernatural                                             | yāo jiǎo                                   | yāo        |                   | yāo        |                      | yāo       |            |             8337 | yao1           |        8337 |   1878 |
| 莉     | white jasmine                                                            | lí chí lì                                  | lì         |                   | lì         |                      | lì        |            |             8289 | li4            |        8289 |   1886 |
| 翰     | writing brush, pen, pencil                                               | hàn                                        | hàn        |                   | hàn        |                      | hàn       |            |             8279 | han4           |        8279 |   1888 |
| 芬     | fragrance, aroma; perfume                                                | fēn                                        | fēn        |                   | fēn        |                      | fēn       |            |             8218 | fen1           |        8218 |   1893 |
| 寺     | court, office; temple, monastery                                         | sì shì                                     | sì         |                   | sì         |                      | sì        |            |             8200 | si4            |        8200 |   1896 |
| 萧     | common artemisia; dejected                                               |                                            | xiāo       |                   | xiāo       | 蕭                   | xiāo      |            |             8097 | xiao1          |        8097 |   1907 |
| 柯     | axe-handle; stalk, bough; surname                                        | kē                                         | kē         |                   | kē         |                      | kē        |            |             8061 | ke1            |        8061 |   1911 |

With no pinyin:

| char   | Definition                    |   JunDaFrequency |   Frequency |   Rank |
|:-------|:------------------------------|-----------------:|------------:|-------:|
| 裏     | inside, interior, within      |                3 |           3 |   7383 |
| 秊     | year; new-years; person's age |                1 |           1 |   7873 |

Number of readings according to different souces:

| ‌  HanyuPinlu<br>XHC1983   |    0 |    1 |   2 |   3 |   4 |   5 |   6 |   All |
|:--------------------------|-----:|-----:|----:|----:|----:|----:|----:|------:|
| 0                         | 1079 |    4 |   0 |   1 |   0 |   0 |   0 |  1084 |
| 1                         | 4040 | 2157 | 157 |   0 |   0 |   0 |   0 |  6354 |
| 2                         |  371 |  291 | 123 |  22 |   0 |   0 |   0 |   807 |
| 3                         |   25 |   34 |  27 |  10 |   0 |   1 |   0 |    97 |
| 4                         |    2 |    3 |   5 |   0 |   1 |   0 |   0 |    11 |
| 5                         |    0 |    0 |   2 |   1 |   1 |   0 |   0 |     4 |
| 6                         |    0 |    0 |   0 |   0 |   0 |   0 |   1 |     1 |
| 7                         |    0 |    1 |   1 |   0 |   0 |   0 |   0 |     2 |
| All                       | 5517 | 2490 | 315 |  34 |   2 |   1 |   1 |  8360 |

| ‌   HanyuPinlu<br>TGHZ2013   |    0 |    1 |   2 |   3 |   4 |   5 |   6 |   All |
|:----------------------------|-----:|-----:|----:|----:|----:|----:|----:|------:|
| 0                           | 1377 |   12 |   1 |   1 |   0 |   0 |   0 |  1391 |
| 1                           | 3940 | 2272 | 183 |   1 |   0 |   0 |   0 |  6396 |
| 2                           |  190 |  192 | 109 |  24 |   0 |   1 |   0 |   516 |
| 3                           |    8 |   14 |  21 |   6 |   0 |   0 |   1 |    50 |
| 4                           |    2 |    0 |   0 |   2 |   1 |   0 |   0 |     5 |
| 5                           |    0 |    0 |   1 |   0 |   0 |   0 |   0 |     1 |
| 6                           |    0 |    0 |   0 |   0 |   1 |   0 |   0 |     1 |
| All                         | 5517 | 2490 | 315 |  34 |   2 |   1 |   1 |  8360 |

| ‌   TGHZ2013<br>XHC1983   |    0 |    1 |   2 |   3 |   4 |   5 |   6 |   All |
|:-------------------------|-----:|-----:|----:|----:|----:|----:|----:|------:|
| 0                        | 1006 |   76 |   2 |   0 |   0 |   0 |   0 |  1084 |
| 1                        |  369 | 5970 |  15 |   0 |   0 |   0 |   0 |  6354 |
| 2                        |   16 |  329 | 462 |   0 |   0 |   0 |   0 |   807 |
| 3                        |    0 |   19 |  34 |  43 |   1 |   0 |   0 |    97 |
| 4                        |    0 |    1 |   2 |   5 |   3 |   0 |   0 |    11 |
| 5                        |    0 |    0 |   0 |   1 |   1 |   1 |   1 |     4 |
| 6                        |    0 |    0 |   0 |   1 |   0 |   0 |   0 |     1 |
| 7                        |    0 |    1 |   1 |   0 |   0 |   0 |   0 |     2 |
| All                      | 1391 | 6396 | 516 |  50 |   5 |   1 |   1 |  8360 |