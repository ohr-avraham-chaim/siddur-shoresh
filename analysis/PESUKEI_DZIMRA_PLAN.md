# Pesukei D'Zimra - Systematic Build Plan

## Project Overview

**Total Estimated Words**: ~3,000+ words
**Sections**: 11 distinct textual units
**Strategy**: Modular approach - build each section as independent JSON file
**Advantage**: Reuse Ashrei (already complete), manageable units, incremental progress

---

## Section Breakdown & Analysis

### Section 1: Mizmor Shir Chanukat HaBayit (Psalm 30)
- **Hebrew Name**: מִזְמור שִׁיר חֲנֻכַּת הַבַּיִת לְדָוִד
- **Estimated Words**: ~150 words
- **Biblical Source**: Tehillim (Psalms) 30
- **Context**: Opening psalm recited daily
- **Complexity**: Medium - standard psalm vocabulary
- **Priority**: Phase 3 (after core framework sections)

### Section 2: Kaddish D'Rabbanan (Rabbinical Kaddish)
- **Hebrew Name**: קדיש דרבנן
- **Estimated Words**: ~80 words
- **Language**: **Aramaic** (not Hebrew!)
- **Context**: Recited after Torah study
- **Complexity**: High - different language, different roots
- **Priority**: Phase 5 (special handling required)
- **Special Note**: Will need Aramaic root system, different from Hebrew

### Section 3: Baruch She'amar (Opening Blessing)
- **Hebrew Name**: בָּרוּךְ שֶׁאָמַר
- **Estimated Words**: ~140 words
- **Type**: Liturgical blessing with multiple "Baruch" statements
- **Context**: Opens Pesukei D'Zimra
- **Complexity**: Medium - repetitive structure (11x "בָּרוּךְ"), blessing formula
- **Priority**: Phase 1 (HIGH - opens entire Pesukei D'Zimra)
- **Key Feature**: 11 "Baruch" statements + closing blessing

### Section 4: Hodu LaHashem (1 Chronicles 16:8-36)
- **Hebrew Name**: הודוּ לה' קִרְאוּ בִשְׁמו
- **Estimated Words**: ~250 words
- **Biblical Source**: Divrei HaYamim (Chronicles I) 16:8-36
- **Context**: King David's song of thanks
- **Complexity**: Medium-High - narrative, historical context
- **Priority**: Phase 3

### Section 5: Mizmor L'Todah (Psalm 100)
- **Hebrew Name**: מִזְמור לְתודָה
- **Estimated Words**: ~40 words
- **Biblical Source**: Tehillim 100
- **Context**: Short thanksgiving psalm
- **Complexity**: Low - short, well-known text
- **Priority**: Phase 1 (HIGH - short, commonly used)

### Section 6: Verse Compilation 1
- **Contains**: Multiple verses from various Psalms
- **Estimated Words**: ~150 words
- **Sources**: Scattered verses (104:31, 113:2, 113:3, 135:13, etc.)
- **Context**: Transitional verses before Ashrei
- **Complexity**: Medium - compilation requires verse attribution
- **Priority**: Phase 3

### Section 7: Ashrei (Psalm 145)
- **Hebrew Name**: אַשְׁרֵי
- **Estimated Words**: 173 words
- **Status**: ✅ **ALREADY COMPLETE**
- **File**: `ashrei_embedded.json`
- **Priority**: DONE - will reference existing file

### Section 8: Psalm 146 (Halleluyah #1)
- **Hebrew Name**: הַלְלוּיָהּ הַלְלִי נַפְשִׁי
- **Estimated Words**: ~85 words
- **Biblical Source**: Tehillim 146
- **Context**: First of 6 Hallel psalms
- **Complexity**: Low-Medium
- **Priority**: Phase 2 (core Hallel sequence)

### Section 9: Psalm 147 (Halleluyah #2)
- **Hebrew Name**: הַלְלוּיָהּ כִּי טוב זַמְּרָה
- **Estimated Words**: ~115 words
- **Biblical Source**: Tehillim 147
- **Context**: Second Hallel psalm
- **Complexity**: Medium
- **Priority**: Phase 2

### Section 10: Psalm 148 (Halleluyah #3)
- **Hebrew Name**: הַלְלוּיָהּ הַלְלוּ אֶת ה' מִן הַשָּׁמַיִם
- **Estimated Words**: ~90 words
- **Biblical Source**: Tehillim 148
- **Context**: Third Hallel psalm - cosmic praise
- **Complexity**: Medium
- **Priority**: Phase 2

### Section 11: Psalm 149 (Halleluyah #4)
- **Hebrew Name**: הַלְלוּיָהּ שִׁירוּ לה' שִׁיר חָדָשׁ
- **Estimated Words**: ~70 words
- **Biblical Source**: Tehillim 149
- **Context**: Fourth Hallel psalm
- **Complexity**: Low-Medium
- **Priority**: Phase 2

### Section 12: Psalm 150 (Halleluyah #5)
- **Hebrew Name**: הַלְלוּיָהּ הַלְלוּ אֵל בְּקָדְשׁו
- **Estimated Words**: ~50 words
- **Biblical Source**: Tehillim 150
- **Context**: Final Hallel psalm - instrumental praise
- **Complexity**: Low - very musical
- **Priority**: Phase 2

### Section 13: Verse Compilation 2
- **Contains**: Closing verses before Shirat HaYam
- **Estimated Words**: ~60 words
- **Sources**: Various verses (Ps 89:53, 135:21, 72:18-19, etc.)
- **Context**: Transition to Song at Sea
- **Complexity**: Low-Medium
- **Priority**: Phase 3

### Section 14: VaYevarech David (David's Blessing)
- **Hebrew Name**: וַיְבָרֶךְ דָּוִיד
- **Estimated Words**: ~80 words
- **Biblical Source**: Divrei HaYamim (1 Chronicles) 29:10-13
- **Context**: David's prayer before Song at Sea
- **Complexity**: Medium
- **Priority**: Phase 3

### Section 15: Atah Hu (You Are Hashem)
- **Hebrew Name**: אַתָּה הוּא ה' לְבַדֶּךָ
- **Estimated Words**: ~180 words
- **Biblical Source**: Nechemiah 9:6-11
- **Context**: Historical narrative before Song at Sea
- **Complexity**: High - long narrative
- **Priority**: Phase 4

### Section 16: VaYoshia (And Hashem Saved)
- **Hebrew Name**: וַיּושַׁע ה'
- **Estimated Words**: ~60 words
- **Biblical Source**: Shemot (Exodus) 14:30-31
- **Context**: Immediate prelude to Song at Sea
- **Complexity**: Low-Medium
- **Priority**: Phase 4

### Section 17: Shirat HaYam (Song at the Sea)
- **Hebrew Name**: אָז יָשִׁיר משֶׁה
- **Estimated Words**: ~800-900 words
- **Biblical Source**: Shemot (Exodus) 15:1-19 + additions
- **Context**: Moses and Israel's song after splitting of Red Sea
- **Complexity**: Very High - longest single text, poetic, archaic language
- **Priority**: Phase 4 (build as single large unit or break into stanzas)
- **Special Note**: Most significant text in Pesukei D'Zimra

### Section 18: Yishtabach (Closing Blessing)
- **Hebrew Name**: יִשְׁתַּבַּח שִׁמְךָ
- **Estimated Words**: ~110 words
- **Type**: Liturgical closing blessing
- **Context**: Concludes entire Pesukei D'Zimra
- **Complexity**: Medium - formal blessing language
- **Priority**: Phase 1 (HIGH - closes Pesukei D'Zimra, pairs with Baruch She'amar)

---

## Build Phases (Systematic Execution Plan)

### Phase 1: Core Framework (HIGH PRIORITY)
**Goal**: Establish opening/closing structure
**Estimated Total**: ~290 words
**Timeline**: Start immediately

1. **Baruch She'amar** (~140 words)
   - Opens Pesukei D'Zimra
   - Repetitive structure (good for template)
   - File: `baruch_sheamar_embedded.json`

2. **Yishtabach** (~110 words)
   - Closes Pesukei D'Zimra
   - Pairs with Baruch She'amar
   - File: `yishtabach_embedded.json`

3. **Mizmor L'Todah (Psalm 100)** (~40 words)
   - Short, complete unit
   - Commonly recited
   - File: `psalm_100_embedded.json`

**Output**: 3 complete texts, framework established

---

### Phase 2: Six Hallel Psalms (CORE CONTENT)
**Goal**: Complete the 6-psalm Hallel sequence
**Estimated Total**: ~410 words
**Timeline**: After Phase 1

1. **Psalm 146** (~85 words) - `psalm_146_embedded.json`
2. **Psalm 147** (~115 words) - `psalm_147_embedded.json`
3. **Psalm 148** (~90 words) - `psalm_148_embedded.json`
4. **Psalm 149** (~70 words) - `psalm_149_embedded.json`
5. **Psalm 150** (~50 words) - `psalm_150_embedded.json`

**Note**: Ashrei (Psalm 145) already complete, so we have 6 consecutive psalms done

**Output**: 5 new texts (6 total Hallel psalms with Ashrei)

---

### Phase 3: Supporting Texts (MEDIUM PRIORITY)
**Goal**: Build historical and transitional sections
**Estimated Total**: ~540 words
**Timeline**: After Phase 2

1. **Psalm 30** (Mizmor Shir) (~150 words) - `psalm_30_embedded.json`
2. **Hodu** (1 Chronicles 16) (~250 words) - `hodu_embedded.json`
3. **Verse Compilation 1** (~80 words) - `pesukei_verses_1_embedded.json`
4. **VaYevarech David** (~80 words) - `vayevarech_david_embedded.json`

**Output**: 4 complete texts

---

### Phase 4: Song at the Sea Complex (LARGE TEXTS)
**Goal**: Build the climactic Song at Sea section
**Estimated Total**: ~1,040 words
**Timeline**: After Phase 3

1. **Atah Hu** (Nechemiah) (~180 words) - `atah_hu_embedded.json`
2. **VaYoshia** (Exodus 14) (~60 words) - `vayoshia_embedded.json`
3. **Shirat HaYam** (Exodus 15) (~800 words) - `shirat_hayam_embedded.json`
   - **Substrategy**: May break into stanzas if too large

**Output**: 3 texts (1 very large)

---

### Phase 5: Special Handling (ARAMAIC)
**Goal**: Handle Aramaic Kaddish with different root system
**Estimated Total**: ~80 words
**Timeline**: Final phase or parallel development

1. **Kaddish D'Rabbanan** (~80 words) - `kaddish_drabbanan_embedded.json`
   - **Special Requirements**:
     - Aramaic roots (different from Hebrew)
     - Different grammatical patterns
     - May need separate root dictionary
   - **Approach**: Use Aramaic-Hebrew cognates where possible

**Output**: 1 Aramaic text with adapted system

---

## Implementation Strategy

### Step 1: File Organization
Create separate source files from `persukei_dezimra_clean.md`:

```
Siddur/
├── source_texts/
│   ├── pesukei_dzimra/
│   │   ├── 01_psalm_30_clean.md
│   │   ├── 02_kaddish_drabbanan_clean.md
│   │   ├── 03_baruch_sheamar_clean.md
│   │   ├── 04_hodu_clean.md
│   │   ├── 05_psalm_100_clean.md
│   │   ├── 06_verses_compilation_1_clean.md
│   │   ├── 07_ashrei_clean.md (already exists)
│   │   ├── 08_psalm_146_clean.md
│   │   ├── 09_psalm_147_clean.md
│   │   ├── 10_psalm_148_clean.md
│   │   ├── 11_psalm_149_clean.md
│   │   ├── 12_psalm_150_clean.md
│   │   ├── 13_verses_compilation_2_clean.md
│   │   ├── 14_vayevarech_david_clean.md
│   │   ├── 15_atah_hu_clean.md
│   │   ├── 16_vayoshia_clean.md
│   │   ├── 17_shirat_hayam_clean.md
│   │   └── 18_yishtabach_clean.md
```

### Step 2: Build Scripts Strategy

**Reusable Components**:
- Standard blessing formula mappings (already have)
- Common psalm vocabulary (build comprehensive dictionary)
- Shared root mappings across texts

**Script Templates**:
1. `build_psalm_template.py` - for Psalms 30, 100, 146-150
2. `build_blessing_template.py` - for Baruch She'amar, Yishtabach
3. `build_narrative_template.py` - for Hodu, Atah Hu, VaYoshia
4. `build_shirat_hayam.py` - custom for Song at Sea (largest text)
5. `build_kaddish.py` - custom for Aramaic text

### Step 3: Vocabulary Management

**Create Master Root Dictionary**:
```python
# scripts/pesukei_root_dictionary.py
PESUKEI_ROOTS = {
    # From existing texts
    **EXISTING_ROOTS,

    # Psalm-specific roots
    "ה-ל-ל": {"meaning": "praise, glory", "type": "verb"},
    "ז-מ-ר": {"meaning": "sing, make music", "type": "verb"},
    "ש-י-ר": {"meaning": "sing, song", "type": "verb/noun"},

    # Shirat HaYam specific
    "ג-א-ה": {"meaning": "pride, rise up", "type": "verb"},
    "ר-מ-ה": {"meaning": "throw, cast", "type": "verb"},

    # Add ~200-300 more roots
}
```

### Step 4: Progressive Build Order

**Week 1: Phase 1** (Foundation)
- Extract source files 3, 5, 18
- Build Baruch She'amar
- Build Mizmor L'Todah (Psalm 100)
- Build Yishtabach
- **Milestone**: Framework complete

**Week 2: Phase 2** (Hallel Core)
- Extract source files 8-12
- Build Psalms 146-150 (one per day or batch)
- **Milestone**: All 6 Hallel Psalms complete (with Ashrei)

**Week 3: Phase 3** (Supporting)
- Extract source files 1, 4, 6, 14
- Build Psalm 30
- Build Hodu
- Build verse compilations
- Build VaYevarech David
- **Milestone**: Historical/transitional sections complete

**Week 4: Phase 4** (Song at Sea)
- Extract source files 15-17
- Build Atah Hu
- Build VaYoshia
- Build Shirat HaYam (may take multiple days)
- **Milestone**: Complete Song at Sea complex

**Week 5: Phase 5** (Aramaic)
- Extract source file 2
- Research Aramaic root system
- Build Kaddish D'Rabbanan
- **Milestone**: All Pesukei D'Zimra complete

### Step 5: Quality Assurance

**After Each Phase**:
1. Verify 100% translation coverage
2. Verify 100% shoresh coverage
3. Update cross-text frequencies
4. Document unique roots discovered
5. Create phase summary

**Final Integration**:
1. Combine all frequencies across 18+ texts
2. Generate master Pesukei D'Zimra statistics
3. Create comprehensive documentation
4. Build master index of all roots

---

## Expected Outcomes

### Quantitative Metrics

**Total System After Pesukei D'Zimra**:
- **Current**: 14 texts, 1,067 words, 280 unique roots
- **After Phase 1**: 17 texts, ~1,357 words, ~320 roots
- **After Phase 2**: 22 texts, ~1,767 words, ~360 roots
- **After Phase 3**: 26 texts, ~2,307 words, ~400 roots
- **After Phase 4**: 29 texts, ~3,347 words, ~450 roots
- **After Phase 5**: 30 texts, ~3,427 words, ~470 roots

**Root Discovery Projection**:
- Psalms typically add 20-30 unique roots each
- Shirat HaYam will add 80-100 unique roots (archaic language)
- Total system will likely reach **450-500 unique roots**

### Qualitative Benefits

1. **Complete Morning Service Coverage**
   - Birkot HaShachar ✅
   - Pesukei D'Zimra ✅ (after completion)
   - Ready for Shema/Amidah

2. **Psalm Expertise**
   - 8 complete Psalms (30, 100, 145-150)
   - Pattern recognition across Tehillim
   - Understanding of Hallel structure

3. **Biblical Narrative Integration**
   - Exodus story (Song at Sea)
   - Chronicles (Hodu, VaYevarech)
   - Nechemiah (Atah Hu)

4. **Linguistic Breadth**
   - Hebrew prayers ✅
   - Biblical poetry ✅
   - Aramaic liturgy ✅

---

## Risk Mitigation

### Challenge 1: Size of Shirat HaYam
**Risk**: 800-900 words may exceed comfortable build limits
**Mitigation**:
- Break into logical stanzas (19 verses + additions)
- Build verse-by-verse
- Extensive testing before full build

### Challenge 2: Aramaic in Kaddish
**Risk**: Different language, different roots
**Mitigation**:
- Research Aramaic-Hebrew cognates
- Build specialized Aramaic root dictionary
- May require different data structure

### Challenge 3: Verse Compilations
**Risk**: Attribution tracking for scattered verses
**Mitigation**:
- Add `source_reference` field to each verse
- Track biblical book + chapter + verse
- Enable cross-referencing

### Challenge 4: Vocabulary Overlap
**Risk**: Many repeated words across 18 texts
**Mitigation**:
- Build comprehensive master root dictionary first
- Reuse mappings across texts
- Track which texts use which roots

### Challenge 5: Token/Memory Limits
**Risk**: Processing very large files
**Mitigation**:
- Build one text at a time
- Incremental testing
- Save frequently

---

## Success Criteria

**Phase 1 Complete When**:
- [ ] Baruch She'amar: 100% translation + shoresh
- [ ] Mizmor L'Todah: 100% translation + shoresh
- [ ] Yishtabach: 100% translation + shoresh
- [ ] All 3 files saved and validated

**Phase 2 Complete When**:
- [ ] Psalms 146-150: Each 100% complete
- [ ] All 5 psalm files saved
- [ ] Hallel sequence documented

**Phase 3 Complete When**:
- [ ] Psalm 30: 100% complete
- [ ] Hodu: 100% complete
- [ ] Verse compilations: 100% complete
- [ ] VaYevarech David: 100% complete

**Phase 4 Complete When**:
- [ ] Atah Hu: 100% complete
- [ ] VaYoshia: 100% complete
- [ ] Shirat HaYam: 100% complete (largest milestone)

**Phase 5 Complete When**:
- [ ] Kaddish D'Rabbanan: 100% complete with Aramaic roots

**Entire Project Complete When**:
- [ ] All 18 texts at 100%
- [ ] Cross-text frequencies updated
- [ ] Master documentation created
- [ ] ~3,400+ words fully analyzed
- [ ] ~470+ unique roots identified

---

## Next Immediate Steps

1. **Extract Source Files** - Split `persukei_dezimra_clean.md` into 18 files
2. **Build Phase 1** - Start with Baruch She'amar (opens Pesukei D'Zimra)
3. **Create Master Root Dictionary** - Compile all known roots + psalm-specific
4. **Document Progress** - Track completion percentage

**Ready to proceed with Step 1: File Extraction?**
