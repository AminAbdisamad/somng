interface NameType {
  name: string;
  age?: number;
}

export const NameTag = ({ name, age }: NameType) => {
  return (
    <div>
      {name} {age}
    </div>
  );
};
