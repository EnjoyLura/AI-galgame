# ======================================================================
# 角色定义
# 所有 Galgame 剧本中出场角色的统一 Character() 声明。
# 与《通用剧本模板.md》中的角色英文代号保持一致。
# ======================================================================

# ---- 主人公（第一人称视角，出声台词时使用）----
define y   = Character("悠真",   color="#6ea8ff")

# ---- 五位可攻略女主（image= 绑定到 images.rpy 中对应的 image tag）----
define chi   = Character("千纱",   color="#ffb3c1", image="chi")    # 七瀬千纱
define aya   = Character("绫音",   color="#c0a0ff", image="aya")    # 白鸟绫音
define natsu = Character("千夏",   color="#ffa0a0", image="natsu")  # 星野千夏
define aka   = Character("茜",     color="#ff9a6c", image="aka")    # 筿崎茜
define haru  = Character("小春",   color="#ffd27f", image="haru")   # 千羽小春（妹妹）

# ---- 男配 ----
define shin  = Character("信",     color="#a0d8a0", image="shin")   # 五十岚信

# ---- 家人（暂无立绘，仅通过台词出场）----
define mom   = Character("妈妈",   color="#e6c0a0")
define dad   = Character("爸爸",   color="#9ab7d8")

# 旁白（主人公心理独白与环境描写）使用 Ren'Py 默认 narrator，无需额外声明。
