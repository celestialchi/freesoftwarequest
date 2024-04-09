from dataclasses import dataclass, field

@dataclass
class Skillset:
    linear_thinking: int
    creativity: int
    hacking_skills: int
    emotional_stability: int
    stamina: int
    luck: int
    charisma: int

@dataclass
class Ability:
    name: str
    description: str
    min_skillset: Skillset

@dataclass
class Project:
    title: str
    description: str
    status: str
    priority: str
    difficulty: int
    min_skillset: Skillset
    required_abilities: list[Ability] = field(default_factory=list)

@dataclass
class GitIssue:
    title: str
    description: str
    status: str
    priority: str
    difficulty: int
    min_skillset: Skillset
    worthless: bool
    required_abilities: list[Ability] = field(default_factory=list)

@dataclass
class GitPullRequest:
    title: str
    description: str
    status: str
    priority: str
    difficulty: int
    min_skillset: Skillset
    worthless: bool
    malicious: bool
    required_abilities: list[Ability] = field(default_factory=list)

@dataclass
class Hacker:
    name: str
    age: int
    abilities: list
    projects: list

@dataclass
class Modifier:
  reason: str
  amount: int

@dataclass
class Skill:
    name: str
    base: int
    modifiers: list[Modifier] = field(default_factory=list)

@dataclass
class TemporaryEffect:
    name: str
    duration: int
    modifiers: list[Modifier] = field(default_factory=list)

@dataclass
class PermanentEffect:
    name: str
    modifiers: list[Modifier] = field(default_factory=list)

@dataclass
class EffectsContainer:
    temporary_effects: list[TemporaryEffect] = field(default_factory=list)
    permanent_effects: list[PermanentEffect] = field(default_factory=list)

@dataclass
class Inventory:
    items: list
    money: int

@dataclass
class Item:
    name: str
    description: str
    value: int

@dataclass
class Store:
    items: list[Item] = field(default_factory=list)

