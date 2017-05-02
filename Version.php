<?php

namespace telesign\sdk\version;

use Composer\Script\Event;
use Composer\Semver\VersionParser;

class Version {

  static function bumpVersion (Event $event) {
    $io = $event->getIO();
    
    if (!is_dir(__DIR__ . "/.git")) {
      $io->writeError("Your local repository is missing.");
      return;
    }
    
    $versionParser = new VersionParser();
    
    $version = $io->askAndValidate("new version: ", function ($answer) use ($versionParser) {
      $versionParser->normalize($answer);
      return $answer;
    });
    
    $confirmed = $io->askConfirmation("Are you sure you want \"$version\" to be the new version of the package? (yes) ");
    
    if (!$confirmed) {
      $io->write("No actions were taken.");
      return;
    }
    
    file_put_contents(__DIR__ . "/src/version/version.php", "<?php

namespace telesign\\sdk\\version;

const VERSION = \"$version\";
", LOCK_EX);

    $tagName = "v" . ltrim($version, "v");

    $result = self::exec([
      "git commit -am \"bump version to $version\"",
      "git tag $tagName",
      "git push",
      "git push --tag"
    ], $stdout, $stderr);
    
    $io->write($stdout);
    
    if (!$result) {
      $io->writeError($stderr);
      return;
    }
    
    $io->write("Done.");
  }
  
  static private function exec ($commands, &$stdout, &$stderr) {
    foreach ($commands as $co) {
      $process = proc_open($co, [
        1 => [ "pipe", "w" ],
        2 => [ "pipe", "w" ]
      ], $pipes);
      
      if (!is_resource($process)) {
        return false;
      }
      
      $stdout[] = trim(stream_get_contents($pipes[1]));
      $stderr = trim(stream_get_contents($pipes[2]));
      $returnCode = proc_close($process);
      
      if ($returnCode !== 0) {
        return false;
      }
    }
    
    return true;
  }

}
