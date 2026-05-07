# ======================================================================
# 共通线 · 第四章：分岐之夜（7月上旬）
# 对应场景表：02_共通线场景表.md - 第7节
# ======================================================================
#
# 本章包含：
#   烟花大会分歧逻辑（共通线 → 个人线 的分支跳转）
#   Bad End（单身线）
#
# 分支规则：
#   if FLAG_AYANE == true AND 选择绫音 → jump ayane_route_start
#   elif FLAG_CHINATSU == true AND 选择千夏 → jump chinatsu_route_start
#   elif FLAG_CHISA == true AND 选择千纱 → jump chisa_route_start
#   elif FLAG_AKANE == true AND 选择茜 → jump akane_route_start
#   elif FLAG_KOHARU >= 2 OR (所有FLAG均为false AND FLAG_KOHARU >= 1) → jump koharu_route_start
#   else → jump bad_end
# ======================================================================


# ----------------------------------------------------------
# 烟花大会分歧逻辑
# ----------------------------------------------------------

# label fireworks_branch:
#     # 根据FLAG和玩家选择，跳转到对应的个人线起点
#     if FLAG_AYANE and selected_route == "ayane":
#         jump ayane_route_start
#     elif FLAG_CHINATSU and selected_route == "chinatsu":
#         jump chinatsu_route_start
#     elif FLAG_CHISA and selected_route == "chisa":
#         jump chisa_route_start
#     elif FLAG_AKANE and selected_route == "akane":
#         jump akane_route_start
#     elif FLAG_KOHARU >= 2 or (not FLAG_AYANE and not FLAG_CHINATSU and not FLAG_CHISA and not FLAG_AKANE and FLAG_KOHARU >= 1):
#         jump koharu_route_start
#     else:
#         jump bad_end


# ======================================================================
# Bad End：单身线
# ======================================================================

label bad_end:

    # [BGM] 孤独·静寂钢琴

    scene bg 悠真房间白天 with fade

    "烟花大会啊……"
    "算了，还是继续做一个旁观者吧。"

    scene bg 悠真房间夜晚 with fade

    "窗外传来烟花的声音。"
    "一下、两下。"
    "（每个人都有一片属于自己的颜色。）"
    "（而我，只是远远地看着。）"

    "第一学期就这样结束了。"
    "什么也没有改变。"

    "如果当初勇敢一点——"
    "是不是会不一样？"

    "（但世上没有后悔药。）"

    scene black with fade
    centered "{size=+8}第一学期·终{/size}"
    centered "{size=+6}在这个夏天，我仍然是一个旁观者。{/size}"

    return
