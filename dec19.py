from math import ceil
from copy import deepcopy

SAMPLE = True

ORE = 'ore'
CLAY = 'clay'
OBSIDIAN = 'obsidian'
GEODE = 'geode'

with open(f"dec19{'-sample' if SAMPLE else ''}.txt") as file:
    blueprints = {}
    for line in file:
        parts = line.rstrip().split(' ')

        blueprints[int(parts[1][:-1])] = {
            ORE: int(parts[6]),
            CLAY: int(parts[12]),
            OBSIDIAN: [int(parts[18]), int(parts[21])],
            GEODE: [int(parts[27]), int(parts[30])],
        }

    print(blueprints)

    parameters_to_process = []

    def bfs(
        blueprint,
        resources,
        robots,
        time,
        skipped_robot,
    ):
        for minute in range(time, 24):
            built_geode_robot = False
            if resources[ORE] >= blueprint[GEODE][0] and resources[OBSIDIAN] >= blueprint[GEODE][1]:
                resources[ORE] -= blueprint[GEODE][0]
                resources[OBSIDIAN] -= blueprint[GEODE][1]
                built_geode_robot = True
                skipped_robot = None

            built_obsidian_robot = False
            if resources[ORE] >= blueprint[OBSIDIAN][0] and resources[CLAY] >= blueprint[OBSIDIAN][1]:
                # wait
                if skipped_robot != OBSIDIAN:
                    new_resources = deepcopy(resources)
                    new_resources[ORE] += robots[ORE]
                    new_resources[CLAY] += robots[CLAY]
                    new_resources[OBSIDIAN] += robots[OBSIDIAN]
                    new_resources[GEODE] += robots[GEODE]
                    parameters_to_process.append([
                        new_resources,
                        deepcopy(robots),
                        minute + 1,
                        OBSIDIAN,
                    ])

                # build
                resources[ORE] -= blueprint[OBSIDIAN][0]
                resources[CLAY] -= blueprint[OBSIDIAN][1]
                built_obsidian_robot = True
                if skipped_robot != OBSIDIAN:
                    skipped_robot = None

            built_clay_robot = False
            if resources[ORE] >= blueprint[CLAY]:
                # wait
                if skipped_robot != CLAY:
                    new_resources = deepcopy(resources)
                    new_resources[ORE] += robots[ORE]
                    new_resources[CLAY] += robots[CLAY]
                    new_resources[OBSIDIAN] += robots[OBSIDIAN]
                    new_resources[GEODE] += robots[GEODE]
                    parameters_to_process.append([
                        new_resources,
                        deepcopy(robots),
                        minute + 1,
                        CLAY,
                    ])

                # build
                resources[ORE] -= blueprint[CLAY]
                if skipped_robot != CLAY:
                    built_clay_robot = True
                skipped_robot = None

            built_ore_robot = False
            if resources[ORE] >= blueprint[ORE]:
                # wait
                if skipped_robot != ORE:
                    new_resources = deepcopy(resources)
                    new_resources[ORE] += robots[ORE]
                    new_resources[CLAY] += robots[CLAY]
                    new_resources[OBSIDIAN] += robots[OBSIDIAN]
                    new_resources[GEODE] += robots[GEODE]
                    parameters_to_process.append([
                        new_resources,
                        deepcopy(robots),
                        minute + 1,
                        ORE,
                    ])

                # build
                resources[ORE] -= blueprint[ORE]
                if skipped_robot != ORE:
                    built_ore_robot = True
                skipped_robot = None

            resources[ORE] += robots[ORE]
            resources[CLAY] += robots[CLAY]
            resources[OBSIDIAN] += robots[OBSIDIAN]
            resources[GEODE] += robots[GEODE]

            if built_geode_robot:
                robots[GEODE] += 1
            if built_obsidian_robot:
                robots[OBSIDIAN] += 1
            if built_clay_robot:
                robots[CLAY] += 1
            if built_ore_robot:
                robots[ORE] += 1
        # print(f'end: {resources}, {robots}')
        return resources, robots


    # print(f'Part One: {part_one_result}')
    # print(f'Part Two: {part_one_result - getTotalSurfaces(airs)}')

    for id, blueprint in blueprints.items():
        print(id)
        print(blueprint)

        parameters_to_process = [[
            { ORE: 0, CLAY: 0, OBSIDIAN: 0, GEODE: 0, },
            { ORE: 1, CLAY: 0, OBSIDIAN: 0, GEODE: 0, },
            0,
            None,
        ]]

        max_result = 0
        best_resources = None
        best_robots = None
        while parameters_to_process:
            parameters = parameters_to_process.pop(0)
            resources, robots = bfs(
                blueprint,
                parameters[0],
                parameters[1],
                parameters[2],
                parameters[3],
            )
            if resources[GEODE] > max_result:
                max_result = resources[GEODE]
                best_resources = resources
                best_robots = robots
            # print(len(parameters_to_process))
            if robots[ORE] == 1 and robots[CLAY] == 4 and robots[OBSIDIAN] == 2:
                print(f'{robots} -> {resources}')

        # print(best_resources)
        # print(best_robots)
        # print(max_result)

        quality_level = id * max_result
        print(quality_level)
        break
