# Pointwise V18.3 Journal file - Thu Dec  3 03:17:18 2020

package require PWI_Glyph 3.18.3

pw::Application setUndoMaximumLevels 5

set _DM(1) [pw::GridEntity getByName dom-1]
set _BL(1) [pw::GridEntity getByName blk-5]
set _DM(2) [pw::GridEntity getByName dom-2]
set _DM(3) [pw::GridEntity getByName dom-3]
set _BL(2) [pw::GridEntity getByName blk-2]
set _DM(4) [pw::GridEntity getByName dom-4]
set _DM(5) [pw::GridEntity getByName dom-5]
set _DM(6) [pw::GridEntity getByName dom-9]
set _BL(3) [pw::GridEntity getByName blk-1]
set _DM(7) [pw::GridEntity getByName dom-10]
set _DM(8) [pw::GridEntity getByName dom-11]
set _DM(9) [pw::GridEntity getByName dom-14]
set _BL(4) [pw::GridEntity getByName blk-3]
set _DM(10) [pw::GridEntity getByName dom-15]
set _DM(11) [pw::GridEntity getByName dom-16]
set _DM(12) [pw::GridEntity getByName dom-19]
set _BL(5) [pw::GridEntity getByName blk-4]
set _DM(13) [pw::GridEntity getByName dom-20]
set _DM(14) [pw::GridEntity getByName dom-21]
set _DM(15) [pw::GridEntity getByName dom-6]
set _DM(16) [pw::GridEntity getByName dom-7]
set _DM(17) [pw::GridEntity getByName dom-8]
set _DM(18) [pw::GridEntity getByName dom-12]
set _DM(19) [pw::GridEntity getByName dom-13]
set _DM(20) [pw::GridEntity getByName dom-17]
set _DM(21) [pw::GridEntity getByName dom-18]
set _DM(22) [pw::GridEntity getByName dom-22]
set _TMP(PW_1) [pw::BoundaryCondition getByName Unspecified]
set _TMP(PW_2) [pw::BoundaryCondition getByName WALL]
set _TMP(PW_3) [pw::BoundaryCondition getByName INLET]
set _TMP(PW_4) [pw::BoundaryCondition getByName OUTLET]
$_TMP(PW_3) apply [list [list $_BL(3) $_DM(6)] [list $_BL(1) $_DM(1)] [list $_BL(2) $_DM(3)] [list $_BL(4) $_DM(9)] [list $_BL(5) $_DM(12)]]
pw::Application markUndoLevel {Set BC}

$_TMP(PW_2) apply [list [list $_BL(3) $_DM(8)] [list $_BL(5) $_DM(14)] [list $_BL(2) $_DM(5)] [list $_BL(4) $_DM(11)]]
pw::Application markUndoLevel {Set BC}

$_TMP(PW_4) apply [list [list $_BL(2) $_DM(4)] [list $_BL(4) $_DM(10)] [list $_BL(3) $_DM(7)] [list $_BL(5) $_DM(13)] [list $_BL(1) $_DM(2)]]
pw::Application markUndoLevel {Set BC}

unset _TMP(PW_1)
unset _TMP(PW_2)
unset _TMP(PW_3)
unset _TMP(PW_4)
