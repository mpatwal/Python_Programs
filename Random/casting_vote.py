class VotingSystem:
    def __init__(self):
        self.vote_count = {}

    def cast_vote(self, candidate_name):

        self.vote_count[candidate_name] = self.vote_count.get(
            candidate_name, 0) + 1

    def get_winner(self):

        if not self.vote_count:
            return []

        max_votes = max(self.vote_count.values())

        max_candidates = []
        for candidate, votes in self.vote_count.items():
            if votes == max_votes:
                max_candidates.append(candidate)

        return sorted(max_candidates)


voting_system = VotingSystem()

voting_system.cast_vote("akshay")
voting_system.cast_vote("simran")
voting_system.cast_vote("raj")
voting_system.cast_vote("simran")
voting_system.cast_vote("simran")
voting_system.cast_vote("simran")
voting_system.cast_vote("raj")
voting_system.cast_vote("raj")
voting_system.cast_vote("raj")
voting_system.cast_vote("akshay")
winners = voting_system.get_winner()
print("Candidate with the maximum votes  --- >  :", winners)
