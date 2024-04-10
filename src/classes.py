from enum import Enum
from dataclasses import dataclass, field
import numpy as np


class Difficulty(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3
    VERY_HARD = 4
    IMPOSSIBLE = 5
    NP_COMPLETE = 6


class IssueStatus(Enum):
    OPEN = 1
    IN_PROGRESS = 2
    COMPLETED = 3
    CLOSED = 4


class PullRequestStatus(Enum):
    OPEN = 1
    IN_PROGRESS = 2
    COMPLETED = 3
    MERGED = 4
    REJECTED = 5


class ProjectStatus(Enum):
    UP_TO_DATE = 1
    OUTDATED = 2
    ABANDONED = 3


class Priority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    URGENT = 4


@dataclass
class Aptitudes:
    linear_thinking: int
    creativity: int
    hacking_skills: int
    emotional_stability: int
    stamina: int
    luck: int
    charisma: int

    def to_numpy(self):
        return np.array(
            [
                self.linear_thinking,
                self.creativity,
                self.hacking_skills,
                self.emotional_stability,
                self.stamina,
                self.luck,
                self.charisma,
            ]
        )


@dataclass
class Skillset:
    problem_solving: int
    data_structures: int
    algorithms: int
    security: int
    networking: int
    hardware: int
    operating_systems: int
    web: int
    databases: int
    github: int
    git: int
    communication: int
    teamwork: int
    leadership: int
    time_management: int
    stress_management: int

    def to_numpy(self):
        return np.array(
            [
                self.problem_solving,
                self.data_structures,
                self.algorithms,
                self.security,
                self.networking,
                self.hardware,
                self.operating_systems,
                self.web,
                self.databases,
                self.github,
                self.git,
                self.communication,
                self.teamwork,
                self.leadership,
                self.time_management,
                self.stress_management,
            ]
        )


@dataclass
class ProblemSolvingStyle:
    name: str
    description: str
    skillset: Skillset

    def to_numpy(self):
        return self.skillset.to_numpy()


@dataclass
class EffectiveSkillset:
    skillset: Skillset
    style: ProblemSolvingStyle

    def to_numpy(self):
        return self.skillset.to_numpy() * self.style.to_numpy()


@dataclass
class Ability:
    name: str
    description: str
    min_skillset: Skillset

    def to_numpy(self):
        return self.min_skillset.to_numpy()


@dataclass
class Project:
    title: str
    description: str
    status: ProjectStatus
    priority: Priority
    difficulty: Difficulty
    min_skillset: Skillset
    required_abilities: list[Ability] = field(default_factory=list)


@dataclass
class GitIssue:
    title: str
    description: str
    status: IssueStatus
    priority: Priority
    difficulty: Difficulty
    min_skillset: Skillset
    worthless: bool
    required_abilities: list[Ability] = field(default_factory=list)


@dataclass
class GitPullRequest:
    title: str
    description: str
    status: PullRequestStatus
    priority: Priority
    difficulty: Difficulty
    min_skillset: Skillset
    worthless: bool
    malicious: bool
    required_abilities: list[Ability] = field(default_factory=list)


@dataclass
class AdditiveAptitudeModifier:
    name: str
    description: str
    aptitudes: Aptitudes

    def to_numpy(self):
        return self.aptitudes.to_numpy()


@dataclass
class AdditiveSkillModifier:
    name: str
    description: str
    skills: Skillset

    def to_numpy(self):
        return self.skills.to_numpy()


@dataclass
class MultiplicativeSkillModifier:
    name: str
    description: str
    skills: Skillset

    def to_numpy(self):
        return self.skills.to_numpy()


@dataclass
class Modifier:
    name: str
    description: str
    aptitude_additions: AdditiveAptitudeModifier
    skill_additions: AdditiveSkillModifier
    skill_multiplications: MultiplicativeSkillModifier

    def to_numpy(self) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        return (
            self.aptitude_additions.to_numpy(),
            self.skill_additions.to_numpy(),
            self.skill_multiplications.to_numpy(),
        )


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


@dataclass
class Hacker:
    name: str
    age: int
    skillset: EffectiveSkillset
    aptitudes: Aptitudes
    inventory: Inventory
    effects: EffectsContainer
    abilities: list[Ability] = field(default_factory=list)
    projects: list[Project] = field(default_factory=list)
    issues: list[GitIssue] = field(default_factory=list)
    pull_requests: list[GitPullRequest] = field(default_factory=list)


@dataclass
class SkillMapping:
    mapping: np.ndarray
