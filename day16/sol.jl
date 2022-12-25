println("Threads: ", Threads.nthreads())
# Run with "julia -t {numThreads} sol.py" to run this file with numThreads threads.
fname = "mini.txt"
fname = "test.txt"
fname = "input.txt"
f = open(fname, "r")
text = read(f, String)
lines = split(text, "\n")[begin:end-1]

struct Node
    name::String
    flow_rate::Int64
    adj # Dict{String,Int64}
end

nodes = []
for i in 1:length(lines)
    line = lines[i] * ","
    words = split(line," ")
    name = words[2]
    rate = parse(Int,words[5][6:end-1])
    neighbors = Dict(words[i][begin:end-1] => 1 for i = 10:length(words))
    push!(nodes,Node(name, rate, neighbors))
end
g = Dict(n.name => n for n in nodes)


# What defines a state?
# 1. the time elapsed
# 2. the current position
# 3. which nodes have been switched on

function index(collection, element)
    for i = 1:length(collection)
        if collection[i] == element
            return i
        end
    end
    return -1
end

function reduce_graph(g)
    zerokeys = []
    for pair in g
        k, n = pair
        if k == "AA"
            continue
        elseif n.flow_rate == 0
            push!(zerokeys, k)
        end
    end

    for key in zerokeys
        n = pop!(g,key)
        for p1 in n.adj
            name1, d1 = p1
            n1 = g[name1]
            pop!(n1.adj, key)
            
            for p2 in n.adj
                name2, d2 = p2
                if name2 == name1
                    continue
                end
                n2 = g[name2]
                direct = 1_000_000
                for pair in n1.adj
                    k,v = pair
                    if k == name2
                        direct = v
                    end
                end
                indirect = d1 + d2
                if indirect < direct
                    n1.adj[name2] = indirect
                    n2.adj[name1] = indirect
                end
            end
        end
    end
end

reduce_graph(g)

ordering = []
for pair in g
    key, val = pair
    push!(ordering,key)
end

time_limit = 30
# fix an ordering
L = length(g)
subsets = 2^L
pressure = []
for i in 1:subsets
    total = 0
    for j in 0:L-1
        name = ordering[j+1]
        total += g[name].flow_rate*(((i-1)>>j)%2)
    end
    push!(pressure, total)
end

function get_answer(time_limit, g, ordering, net_pressure)
    L = length(g)
    subsets = 2^L
    DP = [[[0 for position in 1:L] for config in 1:subsets ] for minute in 1:time_limit+1]
    # it must be backwards for optimality
    # this takes 30*L*(2**L)
    for minute in time_limit:-1:1
        for config in 0:subsets - 1
            for position in 1:L
                initial_benefit = net_pressure[config+1]
                node = g[ordering[position]]
                isOff = (config >>(position-1)) % 2 == 0
                turnOn = DP[minute+1][config + isOff*2^(position-1) + 1][position]
                best = turnOn + initial_benefit
                for pair in node.adj
                    name,pos = pair
                    new_pos = index(ordering, name)
                    travel_time = node.adj[name]
                    if travel_time + minute > time_limit
                        best = max(best, initial_benefit)
                    else
                        alt = travel_time*initial_benefit 
                        alt += DP[minute + travel_time][config+1][new_pos]
                        best = max(best, alt)
                    end
                end
                DP[minute][config+1][position] = best
            end
        end
    end
    return DP[1][1][index(ordering, "AA")]
end
println()
print("Singly Threaded: ")
@time println(get_answer(30, g, ordering, pressure))

function multithreaded(time_limit, g, ordering, net_pressure)
    L = length(g)
    subsets = 2^L
    DP = [[[0 for position in 1:L] for config in 1:subsets ] for minute in 1:time_limit+1]
    # it must be backwards for optimality
    # this takes 30*L*(2**L)
    for minute in time_limit:-1:1
        Threads.@threads for config in 0:subsets - 1
            for position in 1:L
                initial_benefit = net_pressure[config+1]
                node = g[ordering[position]]
                isOff = (config >>(position-1)) % 2 == 0
                turnOn = DP[minute+1][config + isOff*2^(position-1) + 1][position]
                best = turnOn + initial_benefit
                for pair in node.adj
                    name,pos = pair
                    new_pos = index(ordering, name)
                    travel_time = node.adj[name]
                    if travel_time + minute > time_limit
                        best = max(best, initial_benefit)
                    else
                        alt = travel_time*initial_benefit 
                        alt += DP[minute + travel_time][config+1][new_pos]
                        best = max(best, alt)
                    end
                end
                DP[minute][config+1][position] = best
            end
        end
    end
    return DP[1][1][index(ordering, "AA")]
end

println()
print("Multithreaded with ", Threads.nthreads(), " threads: ")
@time println(multithreaded(30, g, ordering, pressure))