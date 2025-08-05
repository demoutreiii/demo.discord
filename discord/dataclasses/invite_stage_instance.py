from .guild_member import GuildMember


class InviteStageInstance(dict):
  @property
  def members(self) -> list[GuildMember]:
    return [GuildMember(data) for data in self["members"]]


  @property
  def participation_count(self) -> int:
    return self["participation_count"]


  @property
  def speaker_count(self) -> int:
    return self["speaker_count"]


  @property
  def topic(self) -> str:
    return self["topic"]