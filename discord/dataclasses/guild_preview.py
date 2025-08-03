from ..enums import GuildFeature
from .asset import Asset
from .emoji import Emoji
from .snowflake import Snowflake
from .sticker import Sticker
from typing import Optional


class GuildPreview(dict):
  @property
  def approximate_member_count(self) -> int:
    return self["approximate_member_count"]


  @property
  def approximate_presence_count(self) -> int:
    return self["approximate_presence_count"]


  @property
  def description(self) -> Optional[str]:
    return self["description"]
  
  
  @property
  def discovery_splash(self) -> Optional[Asset]:
    return Asset(self["discovery_splash"]) if self["discovery_splash"] is not None else None


  @property
  def emojis(self) -> list[Emoji]:
    return [Emoji(data) for data in self["emojis"]]


  @property
  def features(self) -> list[GuildFeature]:
    return [GuildFeatur(name) for name in self["features"]]
  
  
  @property
  def icon(self) -> Optional[Asset]:
    return Asset(self["icon"]) if self["icon"] is not None else None
  
  
  @property
  def id(self) -> Snowflake:
    return Snowflake(self["id"])


  @property
  def name(self) -> str:
    return self["name"]


  @property
  def splash(self) -> Optional[Asset]:
    return Asset(self["splash"]) if self["splash"] is not None else None


  @property
  def stickers(self) -> list[Sticker]:
    return [Sticker(data) for data in self["stickers"]]