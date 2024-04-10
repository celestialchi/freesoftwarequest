import numpy as np
from typing import TypeAlias

Modifiers: TypeAlias = tuple[np.ndarray, np.ndarray, np.ndarray]



def get_additive_effects(effects: np.ndarray) -> np.number:
    return np.sum(effects)


def get_multiplicative_effects(effects: np.ndarray) -> np.number:
    return np.prod(effects)


def get_effective_values(
    base: np.ndarray, additives: np.ndarray, multipliers: np.ndarray
) -> np.ndarray:
    additive_effects = get_additive_effects(additives)
    multiplicative_effects = get_multiplicative_effects(multipliers)
    return ((base + additive_effects) * multiplicative_effects).astype(np.int64)



def map_aptitudes_to_skillpoints(
    aptitudes: np.ndarray, skill_mapping: np.ndarray
) -> np.ndarray:
    return (aptitudes.astype(np.float64) @ skill_mapping).astype(np.int64)

def apply_modifiers(
    apt: np.ndarray, skill_mapping: np.ndarray, modifiers: Modifiers
) -> tuple[np.ndarray, np.ndarray]:
    apt_add = modifiers[0]
    skill_add = modifiers[1]
    skill_mult = modifiers[2]

    effective_aptitudes = get_effective_values(apt, apt_add, np.ones_like(apt_add))
    temp_skills = map_aptitudes_to_skillpoints(effective_aptitudes, skill_mapping)
    effective_skills = get_effective_values(temp_skills, skill_add, skill_mult)

    return (effective_aptitudes, effective_skills)



if __name__ == "__main__":
    from classes import Aptitudes, Skillset, Modifier

    aptitudes = Aptitudes(1, 2, 3, 4, 5, 6, 7)
    aptitude_addition = Aptitudes(1, 0, 1, 0, 0, 0, 0)
    skill_addition = Skillset(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    skill_multiplication = Skillset(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    modifiers = Modifier(
        "test", "test", aptitude_addition, skill_addition, skill_multiplication
    )

    skill_mapping = np.array(
        [
            [1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0],
        ]
    ).astype(np.float64)

    A = aptitudes.to_numpy()
    print(apply_modifiers(A, skill_mapping, modifiers.to_numpy()))
    