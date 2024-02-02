project(ChinesePhoneticIndex LANGUAGES NONE)
cmake_minimum_required(VERSION 3.18)

find_package(Python3 COMPONENTS Interpreter)

file(DOWNLOAD https://unicode.org/Public/UNIDATA/Unihan.zip ${CMAKE_BINARY_DIR}/Unihan.zip SHOW_PROGRESS)
file(ARCHIVE_EXTRACT INPUT ${CMAKE_BINARY_DIR}/Unihan.zip
  DESTINATION ${CMAKE_BINARY_DIR}
  PATTERNS Unihan_Readings.txt Unihan_Variants.txt)

file(DOWNLOAD https://lingua.mtsu.edu/chinese-computing/statistics/char/download.php?Which=MO
  ${CMAKE_BINARY_DIR}/JunDaModern-gb18030.txt SHOW_PROGRESS)
add_custom_command(OUTPUT ${CMAKE_BINARY_DIR}/JunDaModern.txt
  COMMAND ${Python3_EXECUTABLE} -c
  "open('${CMAKE_BINARY_DIR}/JunDaModern.txt', 'w', encoding='utf-8').write(open('${CMAKE_BINARY_DIR}/JunDaModern-gb18030.txt', 'r', encoding='gb18030').read())"
  DEPENDS ${CMAKE_BINARY_DIR}/JunDaModern-gb18030.txt)

option(RELEASE_BUILD "Put the final build artifacts into the ${CMAKE_SOURCE_DIR}/output folder.")

if(RELEASE_BUILD)
  set(OUTPUT_DIR ${CMAKE_SOURCE_DIR}/output)
else()
  set(OUTPUT_DIR ${CMAKE_BINARY_DIR})
endif()

add_custom_command(OUTPUT ${OUTPUT_DIR}/ChPhoneticIndex.dsl ${OUTPUT_DIR}/Dictionary.md
  ${OUTPUT_DIR}/FrequencyTable.md ${OUTPUT_DIR}/Statistics.md
  COMMAND ${Python3_EXECUTABLE} ${CMAKE_SOURCE_DIR}/process_data.py "${CMAKE_BINARY_DIR}" "${OUTPUT_DIR}"
  DEPENDS ${CMAKE_SOURCE_DIR}/process_data.py ${CMAKE_BINARY_DIR}/Unihan_Readings.txt
  ${CMAKE_BINARY_DIR}/Unihan_Variants.txt ${CMAKE_BINARY_DIR}/JunDaModern.txt)

add_custom_target(ChPhoneticIndex.dsl ALL DEPENDS ${OUTPUT_DIR}/ChPhoneticIndex.dsl)
